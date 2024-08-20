from flask import Flask, jsonify, request
from model.definitions_provider import DefinitionsProvider, DefinitionNotFoundException
from model.validation_handler import ValidationHandler
from model.request_handler import RequestHandler

app = Flask(__name__)

# Update the route to include entityName and queryType in the URL path
@app.route('/api/<entityName>/<queryType>', methods=['GET', 'POST'])
def inboundApiHandle(entityName, queryType):
    
    # Get the query parameters and form data
    query_params = request.args.to_dict()
    form_data = request.get_json() if request.is_json else request.form.to_dict()

    try:
        # Get the definition using the getDefinition function
        definitions_provider = DefinitionsProvider()
        definition = definitions_provider.getDefinition(entityName)
        
    except DefinitionNotFoundException as e:
        definition = None
        response_message = str(e)    

    # Validate form data
    validation_handler = ValidationHandler()
    
    if(queryType == 'insert'):
        validation_messages = validation_handler.validate_form_data(definition, form_data)
        if validation_messages:
            return jsonify({"status": "error", "messages": validation_messages}), 400

    http_request_handler = RequestHandler()
    handle_http_request_function = getattr(http_request_handler, queryType)

    if callable(handle_http_request_function):
        if definition:
            if request.method == 'POST' and queryType == 'insert':
                response_payload = handle_http_request_function(definition, form_data)
            else:
                response_payload = handle_http_request_function(definition)
            response_message = "Successful response"
        else:
            response_payload = {}
            response_message = response_message or "Definition not found"
    else:
        response_payload = {}
        response_message = "Query not found"
       
    response = {
        "QueryParams": query_params,
        "FormData": form_data,
        "ResponsePayload": response_payload,
        "Message": response_message,
    }    
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)