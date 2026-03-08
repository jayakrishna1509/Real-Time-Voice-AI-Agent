import whisper
import tempfile

model = whisper.load_model("base")

def speech_to_text(audio_bytes):

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(audio_bytes)
        filename = f.name

    result = model.transcribe(filename)

    return result["text"]