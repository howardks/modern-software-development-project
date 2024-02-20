##
## This is a basic API. Eliza's code will need to be moved to
## this file in such a way that Eliza runs on this server. 
## You can run this server using the terminal command 
## python .\apiServer.py or python3.12 .\apiServer.py
## You can test this server in a browser such as Chrome using
## the URL http://localhost:5000/<endpoint>?input_string=<input text>
## where you replace <endpoint> with the endpoint name and 
## <input text> with your input string. 
## Example: http://localhost:5000/eliza?input_string=hello 
##

from flask import Flask, request, jsonify

app = Flask(__name__)

# This is the example endpoint
@app.route('/process_string', methods=['GET'])
def process_string():
    # Get the string from the GET request
    input_string = request.args.get('input_string')

    # Process the string (for demonstration, just reverse it)
    processed_string = input_string[::-1]

    # Prepare the response
    response = {
        'processed_string': processed_string
    }

    # Return the response as JSON
    return jsonify(response)

# This is the endpoint y'all need to modify to connect to Eliza
@app.route('/eliza', methods=['GET'])
def eliza_endpoint():
    # Get the string from the GET request
    input_string = request.args.get('input_string')

    # Process the string (for demonstration, just reverse it)
    processed_string = input_string[::-1]

    # Prepare the response
    response = {
        'processed_string': processed_string
    }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)