# Kørselsdokumentation: Raspberry Pi 5

### Miljø
- **Hardware:** Raspberry Pi 5 (8GB RAM anbefales)
- **OS:** Raspberry Pi OS (64-bit)

### Konfiguration
Da RPi5 kører på CPU, kræves der ofte længere timeout i `ai_call_http.py`:
```python
response = requests.post(url, json=data, timeout=300)
```

### Resultater
- **Model:** `gemma3:4b`
- **Ydeevne:** Modellen tager længere tid om at "tænke" (First Token Latency er højere end på PC).
- **Status:** Virker! 

## docker compose run --rm ai-app python ai_test.py

```bash
docker compose run --rm ai-app python ai_test.py
Container ai_api-ai-app-run-a829fce99dee Creating 
Container ai_api-ai-app-run-a829fce99dee Created 
Forsøger at kontakte Gemini Cloud (gemini-2.5-flash)...

SVAR FRA CLOUD AI:
Puslingen Luna var en kat med store drømme. Hver nat stirrede hun på den glødende måne og ønskede sig derop. En aften fandt hun en lille, skinnende rumraket i skuret, der virkede til at kalde på hende. Med et modigt hop var hun indenfor.

En tæller startede: "3... 2... 1... AFFYRING!" Med et brøl skød raketten mod den mørke himmel. Luna så jorden blive mindre og mindre, en blå marmorkugle. Snart landede hun blødt i månestøvet. Månen var dækket af glitrende krystaller, og jorden hang smukt på himlen. Luna purrede, hendes drøm var gået i opfyldelse. Hun var den første kat på månen.

## docker compose run --rm ai-app python ai_call_http.py

```bash
mgn@pi5:~/src/ai_api $ docker compose run --rm ai-app python ai_call_http.py
Container ai_api-ai-app-run-0b88a0c1b583 Creating 
Container ai_api-ai-app-run-0b88a0c1b583 Created 
Sender anmodning til: http://host.docker.internal:11434/v1/chat/completions
FULD URL: http://host.docker.internal:11434/v1/chat/completions
LLM_HOST miljøvariabel: host.docker.internal
Okay, here’s a 500-word exploration of the fall of Rome, a process far more complex than a single event, but rather a gradual decline spanning centuries.

---

The fall of the Roman Empire, a phrase that conjures images of barbarian hordes and crumbling legions, is one of the most studied and debated events in Western history. It’s crucial to understand that the “fall” wasn’t a sudden collapse, but a long, protracted process of decline, fragmentation, and ultimately, the transformation of the Western Roman Empire into a collection of successor states.  It wasn’t a singular event, but a cascade of interconnected problems that eroded the foundations of one of history’s greatest empires.

The seeds of Rome's decline were sown long before the final sack of Rome in 476 AD. The 3rd century AD, often referred to as the "Crisis of the Third Century," was a period of intense civil wars, economic instability, and devastating plagues.  Emperors rose and fell with alarming speed, military control fractured, and the empire struggled to maintain its vast territory. This period demonstrated the immense strain on the administrative and military capabilities of Rome.

Several factors contributed to this instability.  **Economic problems** were a key component. Rampant inflation, partly due to debasing the currency, destabilized trade and created widespread poverty. The reliance on slave labor stifled innovation and limited the opportunities for free citizens.  Furthermore, the vast infrastructure projects – roads, aqueducts, and public buildings – consumed enormous amounts of resources, leaving less for the military and the common people.

**Military Overstretch** was another critical issue.  Protecting borders stretching across Gaul, Britain, North Africa, and the Middle East was an incredibly expensive and demanding undertaking. The army, increasingly reliant on Germanic mercenaries – many of whom lacked loyalty to Rome – became less effective and more prone to corruption.  The sheer size of the empire meant that effective governance and communication were severely hindered.

**Political Corruption and Instability** permeated the Imperial system. Frequent civil wars, assassinations, and bureaucratic infighting weakened the central government and undermined public trust. The succession process was notoriously violent and uncertain, leading to power vacuums and further instability. 

However, the arrival of **barbarian migrations** served as the catalyst for the final, irreversible decline of the Western Roman Empire.  Starting in the late 4th century, various Germanic tribes – the Visigoths, Ostrogoths, Vandals, Franks, and Burgundians – were pushed westward by the expanding pressures of the Huns, a nomadic people from Central Asia. Initially, Rome attempted to integrate these groups into the empire, offering land and citizenship in exchange for military service.  

The Battle of Adrianople in 378 AD, where the Visigoths decisively defeated the Roman army, exposed the vulnerability of the Western Roman military. This led to increased pressure and reliance on barbarian mercenaries, which, as noted earlier, proved destabilizing.  Eventually, these tribes, empowered by their successful raids and seeking land within the empire, began to carve out independent kingdoms within the territory of the Western Roman Empire, culminating in the deposition of the last Western Roman Emperor, Romulus Augustulus, in 476 AD.

It's important to note that the **Eastern Roman Empire (Byzantine Empire)**, centered in Constantinople, continued to thrive for another thousand years, preserving Roman culture, law, and traditions. 

The fall of Rome was a complex tapestry woven from internal weaknesses and external pressures. It serves as a potent reminder that even the most powerful empires are susceptible to decline when faced with long-term economic challenges, political instability, and the unexpected forces of migration and warfare. 

```
```