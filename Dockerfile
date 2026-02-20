# Brug et officielt letvægts Python image
FROM python:3.11-slim

# Sæt arbejdsmappen inde i containeren
WORKDIR /app

# Kopier alle filer fra din mappe ind i containeren (inkl. .env og scriptet)
COPY . .

# Installer de nødvendige biblioteker
RUN pip install --no-cache-dir -r requirements.txt

# Kommandoen der køres, når containeren starter
CMD ["python", "ai_test.py"]