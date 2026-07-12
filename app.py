from flask import Flask, render_template, request, jsonify
from chatbot import chat_with_gemini

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({
                "status": False,
                "response": "Message cannot be empty."
            }), 400

        ai_response = chat_with_gemini(user_message)

        return jsonify({
            "status": True,
            "response": ai_response
        })

    except Exception as e:
        return jsonify({
            "status": False,
            "response": f"Error: {str(e)}"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)