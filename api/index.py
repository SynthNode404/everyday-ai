from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    return jsonify({"response": f"You said: {user_input}"})

# Needed by Vercel
def handler(event, context):
    return app(event, context)
