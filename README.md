# run llm from docker

Denne projektmappe indeholder to måder at køre AI på:

| Script | Type | AI Model | Krav |
| :--- | :--- | :--- | :--- |
| **`ai_call_http.py`** | **LOKAL** | `gemma3:4b` | Ollama skal køre lokalt (se `DOCKER_HOWTO.md`) |
| **`ai_test.py`** | **CLOUD** | `gemini-2.5-flash` | Internet + API-nøgle i `.env` |

---

## Hurtig Start

### 1. Kør Lokal AI (Gemma 3)
```bash
# Start Ollama (hvis ikke allerede kører)
docker run -d --name ollama-nuc -p 11434:11434 -v ollama_data:/root/.ollama ollama/ollama
docker exec -it ollama-nuc ollama run gemma3:4b

# Kør scriptet
docker compose run --rm ai-app python ai_call_http.py
```

### 2. Kør Cloud AI (Gemini)
```bash
# Indsæt din nøgle i .env: VITE_API_KEY=xxx
docker compose run --rm ai-app python ai_test.py
```

---

set i denne ![video](https://youtu.be/km5-0jhv0JI)

![Python script displaying HTTP API call to local LLM model with requests library, showing endpoint configuration for llama.cpp v1 chat completions at localhost:12434, data dictionary with ai/smollm2 model and system/user message roles, and response handling with JSON parsing](pictures/ai_http_call.png)

### figur 1: viser ai_call_http.py

````bash
docker model
docker model pull smollm3
docker model list
docker model run smollm3
docker model run gemma3
````

## kør en docker med et python test API kald til en LLM

````bash
docker build -t min-ai-app . && docker run --rm min-ai-app
docker compose run --rm ai-app python ai_test.py

#eller
docker compose up -d --build
docker compose logs -f
docker compose down
````

## to scripts, og de opfører sig vidt forskelligt:

1. Scriptet: ai_test.py (Google Gemini)
- Hvilken model kalder den? gemini-2.5-flash
- Hvor lever modellen? På Googles store servere ude på internettet (i "skyen").
- Skal du starte noget lokalt først? NEJ.
  - Dette script ringer ud af huset via internettet. Så længe du har internet og din API-nøgle, virker det.
1. Scriptet: ai_call_http.py (Lokal Gemma)
- Hvilken model kalder den? docker.io/ai/gemma3:latest
- Hvor lever modellen? På DIN computer (inde i din Docker).
- Skal du starte noget lokalt først? JA! (Du har helt ret).
  - Dette script ringer til "localhost" (din egen maskine). Hvis du ikke har startet serveren, er der ingen, der tager telefonen.

## kør fra docker image term

For at åbne en terminal (command prompt) inde i dit Docker image:

### 1. Med ren Docker kommando

````bash
# Hvis du har bygget billedet som min-ai-app
docker run --rm -it --add-host=host.docker.internal:host-gateway -e LLM_HOST=host.docker.internal min-ai-app /bin/bash
python ai_call_http.py
````

### 2. Med Docker Compose

````bash
# Hvis du bruger docker-compose.yml filen
docker compose run --rm ai-app /bin/bash
python ai_call_http.py
````

### 3. the prompt

````bash
docker compose run --rm ai-app python ai_test.py
````

Det er en kommando, der beder Docker om at udføre en specifik opgave for dig i et rent og isoleret miljø.

Her er hvad de enkelte dele betyder:

1. **docker compose:** Dette er hovedværktøjet. Det kigger i din docker-compose.yml fil for at forstå, hvordan din applikation er bygget op (hvilke services, netværk, miljøvariabler osv.).
2. **run:** Denne del siger: "Jeg vil køre en enkeltstående kommando i en af mine services". Det er perfekt til opgaver som at køre et test-script eller en database-migrering. Det er anderledes end up, som starter og lader køre hele applikationen.

3. **--rm:** Dette er en oprydnings-flag. Det står for "remove" og fortæller Docker: "Når kommandoen er færdig, skal du slette den midlertidige container, du brugte til at køre den". Det forhindrer, at din computer bliver fyldt op med gamle containere.

4. **ai-app:** Dette er navnet på den service, du vil køre kommandoen i. Docker kigger i din docker-compose.yml, finder servicen ai-app og ved, at den skal bruge det Docker-image, der er defineret der (bygget fra din Dockerfile). Den ved også, at den skal indlæse din .env fil, hvilket er afgørende for, at ai_test.py kan få sin API-nøgle.

5. **python ai_test.py:** Dette er selve kommandoen, der skal udføres inde i containeren. Den overskriver standardkommandoen fra din Dockerfile (som er python ai_call_http.py) og kører i stedet dit Google Gemini test-script.

**Kort sagt:**
Kommandoen betyder: "Brug Docker Compose til at starte en ny, midlertidig container for ai-app servicen, kør scriptet ai_test.py inde i den, og slet containeren bagefter."

Det er en utrolig effektiv måde at køre dine scripts på, fordi du er garanteret, at de altid kører i det samme, korrekte miljø med alle de nødvendige biblioteker og konfigurationer, uanset hvilken computer du er på.

### 4. kald til Google Gemini (ai_test.py)

````bash
# start docker container and call script
docker compose run --rm ai-app python ai_test.py

#output
Container ai_api-ai-app-run-246c79107c07 Creating
Container ai_api-ai-app-run-246c79107c07 Created
Forsøger at kontakte Gemini Cloud (gemini-2.5-flash)...

SVAR FRA CLOUD AI:
Der var engang en lille kat ved navn Luna. Hun havde store, drømmende øjne og en hemmelig længsel efter månen.

Hver nat, når alle sov, drømte Luna, at hun byggede en funklende sølvraket. Med et hop var hun inde, og raketten susede opad, forbi stjernerne.

Snart landede hun blødt på den støvede, grå overflade. Der var ingen garnnøgler at lege med, ingen mus at jage. Bare en uendelig stilhed og en betagende udsigt til Jorden, der lyste blåt.

Luna strakte sig, spandt tilfreds og vidste, at hun nu var den eneste kat på månen. Før daggry fløj hun hjem, og vågnede i sin kurv med et smil. Månen var ikke længere bare en prik på himlen; den var hendes hemmelige ven.
````

### 5. kald til http

Dette script kræver en API-nøgle i `.env` filen. Docker Compose håndterer dette automatisk:

````bash
# start gemma3
docker run -d --name ollama-server \
  -p 11434:11434 \
  -v ollama:/root/.ollama \
  ollama/ollama serve

# stop gemma3
docker stop busy_perlman

# test gemma3 is running
curl http://localhost:11434
Ollama is running

# test models
curl http://localhost:11434/api/tags
{"models":[]}

# the call
docker compose run --rm ai-app python ai_call_http.py

# output
Container ai_api-ai-app-run-89c221f7b836 Creating
Container ai_api-ai-app-run-89c221f7b836 Created
Sender anmodning til: http://host.docker.internal:11434/v1/chat/completions
FULD URL: http://host.docker.internal:11434/v1/chat/completions
LLM_HOST miljøvariabel: host.docker.internal
Okay, here’s a 500-word exploration of the fall of Rome, focusing on the complex and multifaceted factors involved – it wasn't a single event, but a gradual decline spanning centuries:

---

The fall of the Roman Empire, a seemingly monolithic event often depicted as a simple collapse, was, in reality, a protracted and agonizing process. While the traditional date of 476 CE marks the deposition of Romulus Augustulus, the last Western Roman Emperor, the seeds of its decline were sown decades, even centuries, earlier. To understand this pivotal moment in Western civilization, we need to recognize a confluence of political, economic, military, and social pressures.

**Political Instability and Corruption:** The Roman Empire had grown accustomed to autocratic rule, but the system gradually eroded. The succession of Emperors was notoriously volatile, often decided through violent power struggles, assassinations, and civil wars. The “Crisis of the Third Century” (235-284 CE) saw a terrifying rapid-fire succession of emperors, many of whom reigned for mere months, destabilizing the government and draining the treasury.  The rise of powerful generals, like Marius and Sulla, who commanded loyal armies instead of serving the state, further undermined the authority of the Senate and centralized control. Corruption became rampant at all levels of government, diminishing public trust and hindering effective administration.

**Economic Woes:** Rome’s vast empire, while initially a source of immense wealth, eventually became a drain on its resources. Constant warfare, lavish building projects (aqueducts, roads, and temples), and the demands of a large, often poorly paid, army stretched the empire’s finances to the breaking point. Excessive taxation, particularly on agriculture, crippled the economy, forcing farmers into poverty and leading to a decline in food production.  Trade, a critical element of Rome’s prosperity, was disrupted by piracy and instability.  Furthermore, the reliance on slave labor stifled innovation and prevented the development of a robust free labor market.

**Military Overstretch and Barbarian Invasions:** The Roman army, once the most efficient and disciplined fighting force in the world, was increasingly burdened by defending a vast and porous border.  The constant need to recruit mercenaries, many of whom were "barbarians" (Germanic tribes, Goths, Vandals, etc.), diluted the army’s quality and loyalty. These tribes, initially seeking trade or refuge within the empire, were steadily drawn in by the empire’s weakness and the promise of land and plunder.  The Visigoths’ devastating sack of Rome in 410 CE, under Alaric, shattered the myth of Roman invincibility.  The Goths, pushed westward by the Huns, eventually established their own kingdoms within the empire’s territories, culminating in the Visigothic Kingdom of Spain.

**Social Decay & Loss of Civic Virtue:**  A decline in social cohesion played a significant role.  The traditional Roman values of civic duty, patriotism, and discipline eroded as luxury and decadence became increasingly prevalent among the wealthy elite. The gap between the rich and the poor widened, creating social unrest and resentment.  The rise of Christianity, while eventually becoming the dominant religion, initially presented a challenge to the established Roman religious order and contributed to a shift in focus away from the state.


Ultimately, the Western Roman Empire succumbed to these combined pressures. The Eastern Roman Empire (Byzantium), with its stronger economy, strategic location, and more effective administration, continued to flourish for another thousand years.  The fall of Rome wasn’t a single dramatic collapse, but a slow, agonizing erosion of power, fueled by internal weaknesses and external threats – a testament to the complex dynamics of empire and its eventual demise.

---

Would you like me to delve deeper into a specific aspect of the fall of Rome, such as a particular period (e.g., the Crisis of the Third Century), a specific group of people (e.g., the Goths), or a specific contributing factor (e.g., economic decline)?
````
