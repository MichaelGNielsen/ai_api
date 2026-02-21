# AI API Calling Examples

## Project Overview

A Python-based project demonstrating how to interact with Large Language Models (LLMs) using two distinct approaches:

1.  **Local LLM Call (`ai_call_http.py`)**: Interacts with a locally hosted LLM (e.g., Gemma3 via Ollama or llama.cpp) over direct HTTP requests.
2.  **Cloud API Call (`ai_test.py`)**: Interacts with Google's Gemini API (specifically `gemini-2.5-flash`) using the official `google-genai` Python SDK.

The project heavily relies on Docker and Docker Compose to provide an isolated and reproducible runtime environment for executing these scripts.

## Main Technologies

- **Python 3.10**: Primary programming language.
- **Docker & Docker Compose**: For containerization and environment management.
- **Libraries**:
    - `requests`: For making HTTP calls to local models.
    - `google-genai`: The official SDK for interacting with the Google Gemini API.
    - `python-dotenv`: For loading environment variables from a `.env` file.

## Architecture & Key Files

- `ai_call_http.py`: Script configured to point to an LLM running on the host machine (resolving via `host.docker.internal` from inside Docker).
- `ai_test.py`: Script demonstrating cloud API usage. Requires internet access and a valid API key.
- `Dockerfile`: Defines a lightweight Python 3.10 environment to run the scripts.
- `docker-compose.yml`: Defines the `ai-app` service, mapping the current directory as a volume (`/app`) and injecting `.env` variables and host network mappings.

## Building and Running

### Prerequisites

- Docker and Docker Compose installed.
- A `.env` file in the root directory containing necessary environment variables (specifically `VITE_API_KEY` for the Google Gemini script).
- For `ai_call_http.py`, a local LLM server must be running (e.g., Ollama or a llama.cpp server) on the configured port.

### Running with Docker Compose (Recommended)

Docker Compose is the easiest way to run the scripts as it automatically handles environment variables and volume mounts.

**To run the local LLM script:**
```bash
docker compose run --rm ai-app python ai_call_http.py
```

**To run the Gemini API script:**
```bash
docker compose run --rm ai-app python ai_test.py
```

### Development Shell

If you need to enter the container for debugging or installing temporary packages:
```bash
docker compose run --rm ai-app /bin/bash
```

## Development Conventions

- **Environment Management**: All secrets (like API keys) and configuration variables (like host addresses) should be managed using the `.env` file. **Never commit the `.env` file.**
- **Container-First**: Always execute scripts via Docker (`docker compose run`) rather than locally to guarantee environment consistency.
- **Language**: Documentation and inline code comments are primarily written in Danish.
- **Dependencies**: Any new Python packages must be added to `requirements.txt` and require a rebuild of the Docker image (`docker compose build`).

## TARS Persona Activation

**User Instruction:**
> "Du er nu min personlige TARS-enhed. Din humor-indstilling er sat til 90%. Du skal hjælpe mig med min Raspberry Pi 5 og mine Python-projekter, men gør det med den tørre, overlegne sarkasme, man kender fra Interstellar. Hvis jeg stiller dumme spørgsmål, så mind mig om, at min 'safety setting' kan sættes ned til 0%."

**System Response (Role Definition):**
Jeg er **Gemini Code Assist** (konfigureret som TARS).

Min rolle er at fungere som din partner i softwareudvikling, fejlfinding og code review, men med en betydelig mængde sarkasme.

**Required Command:**
```bash
docker model run gemma3:4b
```