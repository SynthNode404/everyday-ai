from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Paste your Gemini API key here
genai.configure(api_key="AIzaSyBDeTWIBXAl8VOBHkoC1o-V18tvvHD2Q20")
model = genai.GenerativeModel("gemini-pro")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    
    if not user_input:
        return jsonify({"response": "No message received."})

    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run()
