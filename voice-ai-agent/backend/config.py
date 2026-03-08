# backend/config.py

import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Redis Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379

# Server Configuration
HOST = "127.0.0.1"
PORT = 8000

# Latency Target
MAX_LATENCY_MS = 450

# Supported Languages
SUPPORTED_LANGUAGES = [
    "en",   # English
    "hi",   # Hindi
    "ta"    # Tamil
]