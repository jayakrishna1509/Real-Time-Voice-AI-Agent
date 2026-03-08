import io 
from gtts import gTTS

def text_to_speech(text):

    audio = io.BytesIO()

    tts = gTTS(text=text)

    tts.write_to_fp(audio)

    return audio.getvalue()