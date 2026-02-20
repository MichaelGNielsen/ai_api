import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Hent host fra miljøvariabel eller brug 'localhost' som standard (til lokal kørsel)
llm_host = os.getenv("LLM_HOST", "localhost")
url = f"http://{llm_host}:12434/engines/llama.cpp/v1/chat/completions"

data = {
    "model": "docker.io/ai/gemma3:latest",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Please write 500 words about the fall of Rome."},
    ],
}

try:
    print(f"Sender anmodning til: {url}")
    print(f"FULD URL: {url}")
    print(f"LLM_HOST miljøvariabel: {os.getenv('LLM_HOST')}")
    # Tilføj en timeout for at undgå at scriptet hænger uendeligt
    response = requests.post(url, json=data, timeout=60)
    response.raise_for_status()  # Kaster en fejl ved HTTP-fejlkoder (f.eks. 404, 500)

    # Print modellens svar
    reply = response.json()["choices"][0]["message"]["content"]
    print(reply)

except requests.exceptions.RequestException as e:
    print(f"\nFEJL: Kunne ikke kontakte LLM-serveren: {e}")
except (KeyError, IndexError):
    print("\nFEJL: Modtog et uventet svarformat fra serveren.")
    print("Rå-svar:", response.text)