from fastapi import APIRouter, WebSocket
from services.speech_to_text import speech_to_text
from services.language_detection import detect_language
from agent.agent import process_request
from services.text_to_speech import text_to_speech

router = APIRouter()

@router.websocket("/voice")
async def voice_agent(websocket: WebSocket):
    await websocket.accept()

    while True:

        audio = await websocket.receive_bytes()

        text = speech_to_text(audio)

        language = detect_language(text)

        response = process_request(text, language)

        audio_response = text_to_speech(response)

        await websocket.send_bytes(audio_response)