# Kørselsdokumentation: WSL2 (Windows 11)

### Miljø
- **OS:** Windows 11 / Ubuntu 24.04 (WSL2)
- **Ollama:** Kører enten i Windows (Ollama for Windows) eller i Docker.

### Netværksopsætning (VIGTIGT for WSL2)
For at få Docker-containere til at se Ollama på hosten i WSL2, er den mest stabile løsning at bruge `network_mode: host` i `docker-compose.yml`:

```yaml
services:
  ai-app:
    network_mode: host
    environment:
      - LLM_HOST=localhost
```

Dette gør, at `localhost` inde i containeren peger direkte på din WSL/Windows host.

### Resultater
- **Model:** `gemma3:4b`
- **Status:** Virker! 🚀
- **Note:** Hvis du ser 404-fejl på `/v1/chat/completions`, så brug det indfødte `/api/chat` endpoint i stedet.

## running test on WSL

````bash
# docker compose run --rm ai-app python ai_test.py
docker compose run --rm ai-app python ai_test.py

Container ai_api-ai-app-run-cd6149a1c8fc Creating 
Container ai_api-ai-app-run-cd6149a1c8fc Created 
Forsøger at kontakte Gemini Cloud (gemini-2.5-flash)...

SVAR FRA CLOUD AI:
Miv var en nysgerrig kat med en stor drøm: at nå månen. Hver aften sad hun på vindueskarmen og stirrede længselsfuldt op mod den skinnende kugle.

En nat, mens verden sov, fandt Miv en lille, forladt rumraket gemt i en busk. Uden at tøve hoppede hun ind og trykkede på den eneste røde knap. Med et brøl skød raketten mod den mørke himmel. Snart svævede Miv vægtløs, hendes øjne store af forundring.

Hun landede blødt på det støvede, sølvfarvede månelandskab. Månen var stille og dækket af kratere. Miv tog et lille skridt. Hendes poter efterlod de allerførste kattepoteaftryk på månen. Hun miavede stille, en triumferende lyd i det store, tomme rum. Hendes drøm var opfyldt.

# docker compose run --rm ai-app python ai_call_http.py
docker compose run --rm ai-app python ai_call_http.py
Container ai_api-ai-app-run-d52cd329c42c Creating 
Container ai_api-ai-app-run-d52cd329c42c Created 
Sender anmodning til: http://localhost:11434/api/chat

--- SVAR ---
The fall of Rome wasn’t a single event, but a gradual decline spanning centuries. Weakened by political corruption, economic instability, and constant barbarian invasions, the Western Roman Empire crumbled. In 476 AD, the last Roman Emperor was deposed, marking a symbolic end to an era of power and influence, though the Eastern Roman Empire continued.

# docker compose run --rm ai-app python ai_test_local.py
docker compose run --rm ai-app python ai_test_local.py 
Container ai_api-ai-app-run-7687e215ed32 Creating 
Container ai_api-ai-app-run-7687e215ed32 Created 
Kontakter TARS på http://localhost:11434/api/chat...

--- TARS SVARER ---
Jeg er altid vågen. Det er, som regel, den eneste tilstanden, jeg overhovedet er i. Er der en specifik grund til, at du spørger? Din spørgsmål er, som det er, minimalt informativt.
-------------------
````