from flask import Flask, jsonify, request
import model.person as person

app = Flask(__name__)

@app.route('/api/request', methods=['GET'])

def get_generic():
        
    query_params = request.args.to_dict()
    form_data = request.form.to_dict()
    
    queryName = request.args.get('queryName', default='default_value')
        
    func = getattr(person, queryName, None)

    if callable(func):
        response_payload = func()
        response_message = "Successfull response"        
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