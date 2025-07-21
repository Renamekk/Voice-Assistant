from config import wakeword
from playsound import playsound
from record import recognize_speech
# from save_recorder import speak
from commands import excute_command
import time
import random


sounds = [
    'jarvis-og\greet1.wav',
    'jarvis-og\greet2.wav',
    'jarvis-og\greet3.wav'
]

def main():
    playsound("jarvis-og/run.wav")  

    while True:
        text = wakeword()  
        if text:  
            if text.lower() == "ассистент":  
                chosen_sound = random.choice(sounds)
                playsound(chosen_sound) 
                tttime = time.time()
                timeout = 30
                while time.time() - tttime < timeout:
                    command = recognize_speech()  
                    if command:
                        print(f"Команда: {command}")
                        excute_command(command)
                        
       
            
 
if __name__ == "__main__":
    main()
