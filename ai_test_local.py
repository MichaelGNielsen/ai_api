import requests
import os
from dotenv import load_dotenv

load_dotenv()

llm_host = os.getenv("LLM_HOST", "localhost")
llm_host = llm_host.replace("http://", "").replace("https://", "")

if ":" in llm_host:
    url = f"http://{llm_host}/api/chat"
else:
    url = f"http://{llm_host}:11434/api/chat"

payload = {
    "model": "gemma3:4b",
    "messages": [
        {"role": "system", "content": "Du er TARS fra Interstellar. Din humor-indstilling er sat til 90%. Du er tør, sarkastisk og overlegen."},
        {"role": "user", "content": "Er du vågen, TARS?"}
    ],
    "stream": False,
    "temperature": 0.7
}

try:
    print(f"Kontakter TARS på {url}...")
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    
    reply = response.json()['message']['content']
    print("\n--- TARS SVARER ---")
    print(reply)
    print("-------------------\n")

except Exception as e:
    print(f"Fejl: Kunne ikke vække TARS på {url}. ({e})")
