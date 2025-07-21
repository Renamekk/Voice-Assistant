import os
from playsound import playsound
from record import recognize_speech
from Levenshtein import distance as levenshtein_distance
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
import time
import random
import yaml
import webbrowser

def is_phrase_matched(command, phrases, max_distance=1.5):
    for phrase in phrases:
        if levenshtein_distance(command.lower(), phrase.lower()) <= max_distance:
            return True
    return False


with open('commands.yaml', 'r', encoding='utf-8') as t:
    data = yaml.safe_load(t)

phrases = data.get('phrases', [])
  

def excute_command(command):
    print(f'you say: {command}')
    for item in data.get('list', []):
        phrases = item.get('phrases', [])
        if is_phrase_matched(command, phrases):
            try:
                action = item.get('command', {}).get('action')
                sounds = item.get('voice', {}).get('sounds', [])

                if action == 'ahk':
                    exe_path = item.get('command', {}).get('exe_path')
                    os.startfile(exe_path)

                elif action == 'url':
                    url_path = item.get('command', {}).get('url_path')
                    webbrowser.open(url_path)
                
                elif action == 'joke':
                    jokes = item.get('voice', {}).get('joke_sounds', [])
                    jokes_sound = random.choice(jokes)
                    playsound(jokes_sound)
                
                elif action == 'others':
                    ans = item.get('voice', {}).get('others_sounds', [])
                    ans_sound = random.choice(ans)
                    playsound(ans_sound)

                elif action == 'search-commands':
                    pass
                 

                        



                chosen_sound = random.choice(sounds)
                playsound(chosen_sound)
            except Exception as e:
                print(f'Error: {e}')
                



if __name__ == '__main__':
    while True:
        command = recognize_speech()
        excute_command(command)






