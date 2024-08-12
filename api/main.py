from flask import Flask, jsonify, request
from model.definitionsProvider import getDefinition, DefinitionNotFoundException
import model.queryHandler as queryHandler
app = Flask(__name__)

@app.route('/api/request', methods=['GET'])
def inboundApiHandle():
    
    # Get the query parameters and form data
    query_params = request.args.to_dict()
    
    # Get the queryType and entityName from the query parameters
    form_data = request.form.to_dict()
    
    queryType = request.args.get('queryType', default='default_value')    
    entityName = request.args.get('entityName', default='default_value')        

    try:
        # Get the definition using the getDefinition function
        definition = getDefinition(entityName)
    except DefinitionNotFoundException as e:
        definition = None
        response_message = str(e)

    func = getattr(queryHandler, queryType, None)

    if callable(func):
        if definition:
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