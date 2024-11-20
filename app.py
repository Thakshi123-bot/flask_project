import os
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Define the 'greet' endpoint
@app.route('/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the query string, default to 'World' if not provided
    name = request.args.get('name', 'World')
    # Return a JSON response with a greeting message
    return jsonify({'message': f'Hello, {name}!'})

# Start the server if this script is run directly
if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)
