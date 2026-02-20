# run llm from docker

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
compose run --rm ai-app python ai_test.py

#output
Container ai_api-ai-app-run-006fa536b051 Creating 
Container ai_api-ai-app-run-006fa536b051 Created 
Forsøger at kontakte Gemini (gemini-2.5-flash)...
Misse, en lille stribet kat, elskede at stirre på den store, runde måne om natten. En aften tænkte hun: "Jeg må derop!"

Hun sneg sig ind i et hemmeligt rumlaboratorium og fandt en lille raket. Med et brøl skød den af sted, op gennem skyerne og videre ud i det mørke rum.

Snart landede Misse blødt på Månen. Jorden var en smuk, blå marmorkugle. Misse sprang rundt i det lave tyngdefelt og jagede støvkaniner. Hun fandt endda en bid lækker måneost.

Træt men glad rejste Misse tilbage til sin seng. Hun drømte søde drømme om eventyr blandt stjernerne.
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
Container ai_api-ai-app-run-a1217dc75d0c Creating 
Container ai_api-ai-app-run-a1217dc75d0c Created 
Sender anmodning til: http://host.docker.internal:12434/engines/llama.cpp/v1/chat/completions
Okay, here’s a 500-word exploration of the fall of Rome, aiming to provide a nuanced understanding of a complex and protracted process, rather than a simple “one-cause” explanation:

---

The "fall of Rome" isn’t a single event, but a centuries-long process of decline and transformation that culminated in the collapse of the Western Roman Empire in 476 CE. To understand this dramatic shift, it’s crucial to recognize that Rome didn’t simply “fall”; it morphed, fractured, and ultimately yielded to a complex interplay of internal weaknesses and external pressures.

**The Seeds of Decay (3rd - 5th Centuries):**

By the 3rd century CE, the vast Roman Empire was already showing signs of strain. The Pax Romana, a period of relative peace and prosperity, was fading. Political instability was rampant. Emperors rose and fell rapidly, often through military force, leading to civil wars and a weakening of central authority. The sheer size of the Empire made effective governance increasingly difficult, and the bureaucracy became bloated and corrupt.

Economic woes were equally significant. Constant warfare drained the treasury, while inflation and heavy taxation crippled the middle class. Trade routes were disrupted, and agricultural production declined due to factors like climate change and soil exhaustion. The reliance on slave labor, while initially a source of wealth, ultimately stifled innovation and limited economic mobility.

**External Threats Intensify:**

While internal problems were brewing, external threats steadily escalated. The Germanic tribes – Visigoths, Vandals, Franks, and others – were pushed westward by the Huns, a nomadic group from Central Asia. Initially, Rome attempted to incorporate these tribes as *foederati* (allies), providing them with land in exchange for military service. However, this proved unsustainable.

The Visigoths, after being betrayed by the Roman government, sacked Rome in 410 CE, a profoundly symbolic event that shattered the illusion of Roman invincibility. The Vandals established a kingdom in North Africa, cutting off vital grain supplies to Rome.  The pressure from multiple tribes, coupled with the weakening Roman military, proved too much to bear.

**The Division and the West’s Struggle:**

In 395 CE, the empire was formally divided into Western and Eastern halves. The Eastern Roman Empire, later known as the Byzantine Empire, with its capital in Constantinople, proved far more resilient, benefiting from a more fertile location, a stronger economy, and a more stable political system. The West, however, struggled to maintain control.

The Battle of Adrianople in 378 CE, where the Visigoths decisively defeated a Roman army, exposed the vulnerability of the Western legions and marked a turning point.  The deposition of Romulus Augustulus, the last Western Roman Emperor, in 476 CE by the Germanic chieftain Odoacer, is often cited as the “fall,” but it was more of a symbolic act than a fundamental shift.

**Beyond Military Collapse:**

It's vital to understand that the fall wasn't solely a military affair. The decline was also characterized by:

* **Social Fragmentation:**  The traditional Roman values of civic duty and public service eroded, replaced by a focus on personal wealth and security.
* **Decline in Literacy and Learning:** The loss of patronage from wealthy elites led to a decline in education and scholarship.
* **Rise of Christianity:** While Christianity eventually became the state religion, its early growth arguably challenged traditional Roman beliefs and values, though its impact is debated among historians.


Ultimately, the fall of Rome represents a complex and multifaceted historical process. It wasn't a sudden collapse, but a gradual transformation shaped by internal weaknesses and the unrelenting pressure of external forces. The legacy of Rome – its laws, language, architecture, and political ideas – continued to shape Europe for centuries to come, even as the Western Empire faded into memory.

---

Would you like me to delve deeper into a specific aspect of the fall of Rome, such as the role of the Huns, the economic factors, or the Byzantine Empire’s survival?
````
