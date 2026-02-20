import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("VITE_API_KEY")
if not api_key:
    print("FEJL: Kunne ikke finde VITE_API_KEY i .env filen.")
    exit(1)

# Vi bruger v1beta, da det ofte er her de nyeste modeller som Flash lever
client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta'})

# Definer prompten (spørgsmålet eller instruktionen til modellen)
prompt = "Skriv en kort historie om en kat, der rejser til månen. Historien skal være omkring 100 ord."

# Generer svaret
try:
    print("Forsøger at kontakte Gemini (gemini-2.5-flash)...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Udskriv svaret
    print(response.text)

except Exception as e:
    print(f"\nDER OPSTOD EN FEJL: {e}")
    print("\n--- DEBUG INFO: TILGÆNGELIGE MODELLER ---")
    try:
        # List alle tilgængelige modeller for at se, hvad vi har adgang til
        for model in client.models.list():
            print(f" - {model.name}")
    except Exception as list_error:
        print(f"Kunne ikke hente modelliste: {list_error}")
 