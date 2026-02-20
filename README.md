# run llm from docker

set i denne ![video](https://youtu.be/km5-0jhv0JI)

![Python script displaying HTTP API call to local LLM model with requests library, showing endpoint configuration for llama.cpp v1 chat completions at localhost:12434, data dictionary with ai/smollm2 model and system/user message roles, and response handling with JSON parsing](pictures/ai_http_call.png)

### figur 1: viser ai_http_call.py

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

## latest prompt

````bash
docker compose build --no-cache && docker compose up

docker build --no-cache -t min-ai-app . && docker run --rm min-ai-app

>output
Forsøger at kontakte Gemini (gemini-2.5-flash)...
Luna, en lille, nysgerrig kat, elskede at kigge på den store, runde måne om natten. En aften fandt hun en mystisk, skinnende genstand i haven – en forladt raket! Uden at tøve hoppede hun ind i cockpittet.    

Med et blødt miav trykkede hun på en rød knap. Raketten brølede til live og skød opad, forbi stjerner og glimtende planeter. Snart landede Luna blødt på Månens støvede overflade. Hun jagede månestøvkaniner og kiggede forbavset på Jorden, der lyste blåt i det fjerne.

Da hendes eventyr var slut, fløj Luna hjem igen. Træt, men lykkelig, krøllede hun sig sammen i sin kurv, mens pelsen stadig glimtede af månestøv.
````

## kør fra docker image term

For at åbne en terminal (command prompt) inde i dit Docker image:

### 1. Med ren Docker kommando

````bash
# Hvis du har bygget billedet som min-ai-app
docker run --rm -it min-ai-app /bin/bash 
````

### 2. Med Docker Compose

````bash
# Hvis du bruger docker-compose.yml filen
docker compose run --rm ai-app /bin/bash
````
