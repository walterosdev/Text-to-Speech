from gtts import gTTS
from pathlib import Path
from datetime import datetime
import os

class TextToSpeechService:
    def __init__(self, language="es"):
        self.language = language

    def save_audio(self, text):
        folder = Path("audios")
        folder.mkdir(exist_ok=True)

        filename = f"audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        path = folder / filename

        tts = gTTS(text=text, lang=self.language)
        tts.save(path)

        return path

    def play_audio(self, path):
        os.system(f"{path}")