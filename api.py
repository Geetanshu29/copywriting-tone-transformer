import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_copy(prompt,
                  temperature,
                  top_p):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {

        "model": "deepseek/deepseek-chat-v3-0324",

        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],

        "temperature": temperature,

        "top_p": top_p

    }

    response = requests.post(URL,
                             headers=headers,
                             json=data)

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]