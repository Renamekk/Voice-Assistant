from vosk import Model, KaldiRecognizer
import json, pyaudio
from Levenshtein import distance as levenshtein_distance
from env import WAKE_WORD
# from save_recorder import speak
import pyttsx3
import playsound


model = Model("vosk-model-small-ru-0.22")
engine = pyttsx3.init()


def is_wake_word_detected(recognized_text, wake_word, max_distance=2):
    from Levenshtein import distance as levenshtein_distance
    return levenshtein_distance(recognized_text.lower(), wake_word.lower()) <= max_distance


# Listen for a wakeword
def wakeword():
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    print("Ожидаю ключевое слово...")

    # Wakeword is listened


    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            ans = json.loads(recognizer.Result())
            text = ans.get("text", "")

            if is_wake_word_detected(text, WAKE_WORD):
                print('К вашим услугам сэр')
                return text
     




                
                
                



