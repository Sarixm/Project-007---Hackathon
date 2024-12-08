# This is the local server for each area (e.x class) which would detect the given people which are needed to be detected

from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/api/get', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET request"})

@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "This is a POST request", "data": data})

@app.route('/')
def home():
    return "Hello from the backend server!"

server_port = os.getenv('SERVER_PORT', 5000)

print(f"Backend server is running on port {server_port}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=server_port)