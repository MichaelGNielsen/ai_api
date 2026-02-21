import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Hent host fra miljøvariabel
llm_host = os.getenv("LLM_HOST", "localhost")

# Fjern http:// hvis det er der, så vi selv kan styre det
llm_host = llm_host.replace("http://", "").replace("https://", "")

# Tjek om der allerede er en port (f.eks. :11434) i navnet
if ":" in llm_host:
    url = f"http://{llm_host}/api/chat"
else:
    url = f"http://{llm_host}:11434/api/chat"

data = {
    "model": "gemma3:4b",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Please write 500 words about the fall of Rome."},
    ],
    "stream": False
}

try:
    print(f"Sender anmodning til: {url}")
    response = requests.post(url, json=data, timeout=300)
    response.raise_for_status()

    reply = response.json()["message"]["content"]
    print("\n--- SVAR ---")
    print(reply)

except Exception as e:
    print(f"\nFEJL: Kunne ikke kontakte LLM-serveren på {url}: {e}")
