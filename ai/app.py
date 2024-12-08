# This is the local server for each area (e.x class) which would detect the given people which are needed to be detected

from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def home():
    return "Hello from the AI server!"

@app.route('/api/get', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a GET request"})

@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "This is a POST request", "data": data})

if __name__ == '__main__':
    ai_server_port = int(os.getenv('AI_SERVER_PORT', 5000))  # Read port from .env file
    print(f"AI server is running on port {ai_server_port}")
    app.run(host='0.0.0.0', port=ai_server_port)