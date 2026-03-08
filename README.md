# Voice-AI-Agent

# Real-Time Multilingual Voice AI Agent

## Clinical Appointment Booking System

A real-time conversational **Voice AI Agent** designed for healthcare platforms to automatically manage patient appointments through voice conversations.

The system accepts **voice input**, understands user intent using AI, manages appointment scheduling, and responds with **voice output** — all with **low latency and multilingual support**.

---

# Project Overview

This project implements a **real-time AI voice assistant** capable of managing the complete appointment lifecycle:

• Book appointments

• Cancel appointments

• Reschedule appointments

• Check doctor availability

• Suggest alternative time slots

The assistant supports **multilingual voice interaction** and maintains conversation context to provide a natural user experience.

---

# Key Features

### Real-Time Voice Interaction

Patients can interact with the AI assistant through voice in real time.

### Multilingual Support

Supports three languages:

| Language | Script Example                                    |
| -------- | ------------------------------------------------- |
| English  | "Book appointment with cardiologist"              |
| Hindi    | "मुझे कल डॉक्टर से मिलना है"                      |
| Tamil    | "நாளை மருத்துவரை பார்க்க வேண்டும்"               |

The system automatically detects the language and responds accordingly.

### Contextual Memory

Two types of memory are implemented:

**Session Memory**
Stores conversation context during an active interaction.

Example:
User: Book appointment
Agent: Which doctor?
User: Cardiologist

**Persistent Memory**
Stores patient preferences and appointment history.

Example:
Preferred language
Past appointments
Doctor preference

---

# System Architecture

The voice pipeline follows this architecture:

```
User Speech
     ↓
Speech-to-Text (STT)
     ↓
Language Detection
     ↓
AI Agent (LLM)
     ↓
Tool Orchestration
     ↓
Appointment Service
     ↓
Text Response
     ↓
Text-to-Speech (TTS)
     ↓
Audio Response
```

---

# Tech Stack

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | AI services and backend logic |
| FastAPI           | Backend API server            |
| WebSockets        | Real-time voice communication |
| Redis             | Session memory storage        |
| Whisper           | Speech-to-text conversion     |
| LangDetect        | Language detection            |
| gTTS              | Text-to-speech synthesis      |
| HTML + JavaScript | Voice interaction frontend    |

---

# Project Structure

```
voice-ai-agent
│
├── backend
│   ├── main.py
│   ├── websocket.py
│   └── config.py
│
├── agent
│   ├── agent.py
│   ├── tools.py
│   └── prompt.py
│
├── services
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   └── language_detection.py
│
├── memory
│   ├── session_memory.py
│   └── persistent_memory.py
│
├── scheduler
│   └── appointment_engine.py
│
├── frontend
│   └── index.html
│
├── database
│   └── db.py
│
└── docs
```
---

# Setup Instructions
---

### 1. Create virtual environment


python -m venv venv


Activate:

Windows


venv\Scripts\activate




### 2. Install dependencies


pip install -r requirements.txt


---

### 3. Start Redis server


redis-server


---

### 4. Run the backend server


uvicorn backend.main:app --reload


Server runs at:


http://127.0.0.1:8000


---

### 5. Open frontend

Open:

frontend/index.html


Allow microphone access and start interacting with the voice assistant.

---

# Latency Breakdown

Target system latency: **< 450 ms**

Approximate breakdown:

| Stage           | Time    |
| --------------- | ------- |
| Speech-to-Text  | ~120 ms |
| Agent Reasoning | ~200 ms |
| Text-to-Speech  | ~100 ms |

Total expected latency: **~420 ms**

Latency is logged during request processing.

---

# Error Handling

The system gracefully handles common scenarios:

• Invalid appointment requests
• Scheduling conflicts
• Doctor unavailability
• Speech recognition failures

Example fallback response:

"I'm having trouble understanding your request. Could you please repeat?"

---

# Example Conversation

Patient:
"Book appointment with cardiologist tomorrow"

Agent:
"Your appointment with the cardiologist is available at 10:30 AM. Should I confirm it?"

Patient:
"Yes"

Agent:
"Your appointment has been successfully booked."

---

# Known Limitations

• Basic rule-based intent recognition (can be improved with full LLM integration)

• Simplified scheduling engine

• Limited persistent storage implementation

• Whisper model may increase initial loading time

---

# Future Improvements

• Streaming speech recognition

• Advanced LLM tool calling

• Cloud deployment with Docker

• Horizontal scalability

• Background job queues for outbound campaigns

• Improved multilingual NLP

---

# Conclusion

This project demonstrates the design and implementation of a **Real-Time Multilingual Voice AI Agent** for clinical appointment management. By combining speech recognition, AI-driven reasoning, tool orchestration, and text-to-speech synthesis into a unified pipeline, the system delivers a seamless voice-based experience for patients across multiple languages.

The architecture prioritizes **low latency**, **modularity**, and **contextual awareness** — making it well-suited for real-world healthcare environments where responsiveness and accuracy are critical. The separation of concerns across the agent, memory, scheduler, and service layers ensures the system is maintainable and extensible.

With further enhancements such as full LLM tool calling, streaming STT, and cloud-native deployment, this system can scale to serve large patient populations and support a wide range of clinical workflows beyond appointment booking.