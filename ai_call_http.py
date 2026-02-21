import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Hent host fra miljøvariabel eller brug 'localhost' som standard (til lokal kørsel)
llm_host = os.getenv("LLM_HOST", "localhost")
# Ollama bruger port 11434 og har et OpenAI-kompatibelt endpoint på /v1/chat/completions
url = f"http://{llm_host}:11434/v1/chat/completions"

data = {
    "model": "gemma3:4b",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Please write 500 words about the fall of Rome."},
    ],
}

try:
    print(f"Sender anmodning til: {url}")
    print(f"FULD URL: {url}")
    print(f"LLM_HOST miljøvariabel: {os.getenv('LLM_HOST')}")
    # Tilføj en længere timeout for at give den lokale model tid til at tænke (især på CPU)
    response = requests.post(url, json=data, timeout=300)
    response.raise_for_status()  # Kaster en fejl ved HTTP-fejlkoder (f.eks. 404, 500)

    # Print modellens svar
    reply = response.json()["choices"][0]["message"]["content"]
    print(reply)

except requests.exceptions.RequestException as e:
    print(f"\nFEJL: Kunne ikke kontakte LLM-serveren: {e}")
except (KeyError, IndexError):
    print("\nFEJL: Modtog et uventet svarformat fra serveren.")
    print("Rå-svar:", response.text)