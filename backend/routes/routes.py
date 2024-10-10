from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Flask backend!"

# Route to handle POST requests with JSON data
@main.route('/data', methods=['POST'])
def handle_data():
    data = request.json
    return jsonify({"message": "Data received", "data": data})

# Route to handle URL parameters in GET request
@main.route('/user/<username>')
def greet_user(username):
    return f"Hello, {username}!"
