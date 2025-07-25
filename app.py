from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows GitHub Pages to access your backend

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    return jsonify({"response": f"You said: {user_input}"})

if __name__ == '__main__':
    app.run()
