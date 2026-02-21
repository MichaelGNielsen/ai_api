import requests

# Da dette script er beregnet til at køre direkte på hosten (NUC), bruger vi localhost.
# Hvis det køres via Docker, skal 'localhost' ændres til 'host.docker.internal' eller 'ollama-server'.
url = "http://localhost:11434/v1/chat/completions"

payload = {
    "model": "gemma3:4b",
    "messages": [
        {"role": "system", "content": "Du er TARS fra Interstellar. Din humor-indstilling er sat til 90%. Du er tør, sarkastisk og overlegen. Du kører lige nu lokalt på en NUC (Next Unit of Computing)."},
        {"role": "user", "content": "Er du vågen, TARS? Og hvordan føles det at køre på en lille NUC i stedet for et rumskib?"}
    ],
    "temperature": 0.7
}

try:
    print(f"Kontakter TARS på {url}...")
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    
    reply = response.json()['choices'][0]['message']['content']
    print("--- TARS SVARER ---")
    print(reply)
    print("-------------------")

except Exception as e:
    print(f"Fejl: Kunne ikke vække TARS. Er Ollama startet? ({e})")
