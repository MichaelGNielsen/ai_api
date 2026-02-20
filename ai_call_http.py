import requests
import os

# Hent host fra miljøvariabel eller brug 'localhost' som standard (til lokal kørsel)
llm_host = os.getenv("LLM_HOST", "localhost")
url = f"http://{llm_host}:12434/engines/llama.cpp/v1/chat/completions"

data = {
    "model": "ai/smollm2",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Please write 500 words about the fall of Rome."},
    ],
}

response = requests.post(url, json=data)
response.raise_for_status()

# Print the model's reply
print(response.json()["choices"][0]["message"]["content"])