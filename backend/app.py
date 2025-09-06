from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Rasa endpoint (make sure Rasa is running with --enable-api)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/')
def home():
    return render_template("index.html")  # make sure templates/index.html exists

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Send message to Rasa
        response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})

        if response.status_code != 200:
            return jsonify({"error": "Rasa server not reachable"}), 500

        rasa_response = response.json()

        # Extract bot replies
        bot_replies = [msg.get("text") for msg in rasa_response if "text" in msg]

        return jsonify({"responses": bot_replies})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

