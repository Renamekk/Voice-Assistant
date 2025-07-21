from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("vosk-model-small-ru-0.22")


def recognize_speech():
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,
                      input=True, frames_per_buffer=8000)
    stream.start_stream()

    print("Слушаю...")

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                return text
