from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

CHAT_API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
REFERER = "https://yajat.com"
TITLE = "YajatAI"

def ask_bot(message):
    headers = {
        "Authorization": f"Bearer {CHAT_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": REFERER,
        "X-Title": TITLE,
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "max_tokens": 1000,
        "messages": [
            {"role": "system", "content": "You are a helpful and smart assistant."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {response.status_code}: {response.text}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400
    
    reply = ask_bot(user_input)
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)