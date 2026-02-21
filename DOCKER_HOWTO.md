# Ollama Docker Cheat Sheet

Denne guide beskriver, hvordan du kører Ollama i Docker og administrerer dine lokale sprogmodeller.

## 1. Opsætning af Ollama Container
Kør denne kommando for at starte Ollama-serveren (navngivet `ollama-nuc`):

```bash
docker run -d \
  --name ollama-nuc \
  -v ollama_data:/root/.ollama \
  -p 11434:11434 \
  --restart always \
  ollama/ollama
```

## 2. Model Styring (Gemma 3:4b)

### Download og kør en model
For at køre `gemma3:4b` første gang (henter den automatisk):
```bash
docker exec -it ollama-nuc ollama run gemma3:4b
```

### Liste over hentede modeller
```bash
docker exec -it ollama-nuc ollama list
```

### Fjern en model
```bash
docker exec -it ollama-nuc ollama rm gemma3:4b
```

## 3. Container Administration

### Start / Stop container
```bash
docker stop ollama-nuc
docker start ollama-nuc
```

### Se logs (god til fejlfinding)
```bash
docker logs -f ollama-nuc
```

### Tjek om den svarer (API test)
```bash
curl http://localhost:11434/api/tags
```

## 4. Kørsel af projektets scripts

Det anbefales at bruge **Docker Compose**, da det automatisk håndterer netværk og miljøvariabler.

### Den lette måde (Compose)
```bash
# Kør lokal Gemma 3 test
docker compose run --rm ai-app python ai_call_http.py

# Kør Cloud Gemini test
docker compose run --rm ai-app python ai_test.py
```

### Den manuelle måde (Rå Docker)
Hvis du ikke vil bruge compose, skal du manuelt mappe host-netværket:
```bash
docker build -t ai-api-app .
docker run --rm \
  --add-host=host.docker.internal:host-gateway \
  --env-file .env \
  ai-api-app python ai_call_http.py
```
