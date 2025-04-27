import requests
import os


GROQ_API_KEY = "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"

def get_response(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",  # You can also use "mixtral-8x7b-32768"
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Sorry, something went wrong. Try again."
