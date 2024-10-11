from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS to allow communication with the React frontend

COMPASS_API_URL = "https://dev.compass.tabiya.tech/api/chat"
COMPASS_API_KEY = "compass_api_key"  # Compass API key

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")

    # Make a request to Compass AI API
    response = requests.post(
        COMPASS_API_URL,
        headers={"Authorization": f"Bearer {COMPASS_API_KEY}"},
        json={"message": user_message}
    )

    chatbot_reply = response.json()
    return jsonify(chatbot_reply)  # Send the chatbot's response back to the frontend

if __name__ == "__main__":
    app.run(debug=True)
