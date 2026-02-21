import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Dette script bruger Google Gemini API (Cloud)
# Se ai_call_http.py for lokal kørsel med Gemma 3 via Ollama

api_key = os.getenv("VITE_API_KEY")
if not api_key:
    print("FEJL: Kunne ikke finde VITE_API_KEY i .env filen.")
    exit(1)

client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta'})

prompt = "Skriv en kort historie om en kat, der rejser til månen. Historien skal være omkring 100 ord."

try:
    print("Forsøger at kontakte Gemini Cloud (gemini-2.5-flash)...")
    # Bemærk: For at køre Gemma 3 lokalt, brug ai_call_http.py
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nSVAR FRA CLOUD AI:")
    print(response.text)

except Exception as e:
    print(f"\nDER OPSTOD EN FEJL: {e}")

 