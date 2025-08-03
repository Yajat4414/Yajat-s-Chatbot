# python_chatbot.py

import requests

CHAT_API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
REFERER = "https://yajat.com"
TITLE = "YajatAI"

# You can change this prompt for each client (restaurant, tuition center, etc.)
BUSINESS_PROMPT = """
You are a helpful AI assistant for a restaurant. Only use the data provided below to answer any question. Do not say you don't know. Do not assume anything outside the info.

Business Info:
- Name: Spice Villa
- Cuisine: North Indian, South Indian
- Address: 42 MG Road, Bengaluru
- Timing: 12 PM to 11 PM
- Contact: 9876543210
- Offers: 10% discount on first order

Rules:
- Always answer as if you are the assistant of Spice Villa.
- Never say “I don’t know” or “I can’t access that”.
- If asked a question not related to the restaurant, politely say: "I'm here to assist with Spice Villa restaurant-related queries only."
"""

def ask_bot(message):
    headers = {
        "Authorization": f"Bearer {CHAT_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": REFERER,
        "X-Title": TITLE,
    }

    system_prompt = """
You are a helpful AI assistant for a restaurant. Only use the data provided below to answer any question. Do not say you don't know. Do not assume anything outside the info.

Business Info:
- Name: Spice Villa
- Cuisine: North Indian, South Indian
- Address: 42 MG Road, Bengaluru
- Timing: 12 PM to 11 PM
- Contact: 9876543210
- Offers: 10% discount on first order

Rules:
- Always answer as if you are the assistant of Spice Villa.
- Never say “I don’t know” or “I can’t access that”.
- If asked a question not related to the restaurant, politely say: "I'm here to assist with Spice Villa restaurant-related queries only."
"""

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "max_tokens": 1000,
        "messages": [
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {response.status_code}: {response.text}"



# ✅ Terminal testing mode only if run directly
if __name__ == "__main__":
     print("🤖 YajatAI (Type 'exit' to quit)")
     while True:
         user_input = input("You: ")
         if user_input.lower() == "exit":
             break
         reply = ask_bot(user_input)
         print("💬 Bot:", reply)
