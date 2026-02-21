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
- **Status:** Virker! 🍓
