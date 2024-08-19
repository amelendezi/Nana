from flask import Flask, jsonify, request
from model.definitionsProvider import getDefinition, DefinitionNotFoundException
import model.queryHandler as queryHandler

app = Flask(__name__)

# Update the route to include entityName and queryType in the URL path
@app.route('/api/<entityName>/<queryType>', methods=['GET', 'POST'])
def inboundApiHandle(entityName, queryType):
    
    # Get the query parameters and form data
    query_params = request.args.to_dict()
    form_data = request.form.to_dict()

    try:
        # Get the definition using the getDefinition function
        definition = getDefinition(entityName)
    except DefinitionNotFoundException as e:
        definition = None
        response_message = str(e)

    func = getattr(queryHandler, queryType, None)

    if callable(func):
        if definition:
            if request.method == 'POST' and queryType == 'insert':
                response_payload = func(definition, form_data)
            else:
                response_payload = func(definition)
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