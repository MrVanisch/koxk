import pyautogui as pt
import pyautogui
import time 
import requests
import json
import webbrowser
import os
import datetime

nudes = ""
token = ""

class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)
            pt.moveTo(position[0] , position[1] , duration=self.speed)
            pt.click()
            return 0

        except:
            return 1

def wiadomosc_dioscrd(idkanalu):
    time.sleep(10)
    global nudes
    global token
    start = Clicker('images\kod.png', speed=.8)
    confirm = Clicker('images\kp.png', speed=.8)
    while True: 
        headers1 = {
            'authorization': token
        }
        r = requests.get(f'https://discord.com/api/v9/channels/{idkanalu}/messages',headers=headers1)
        jsonn = json.loads(r.text)
        for value in jsonn: 
            id = int(value['id'])  
            if(int(value['id']) < id):
                id = value['id']
                kod = value['content']
            elif(id == int(value['id'])):
                kod = value['content']
                break
            else:
                kod = value['content']
                break

        if(nudes!=kod and kod != '<@&862297210828881930>' and kod !=''):
            x = datetime.datetime.now()
            print("Kod:", kod, x.strftime("%X %x"))
            webbrowser.open('https://key-drop.com/pl/')
            while start.nav_to_image() == 1:
                time.sleep(2)
            while confirm.nav_to_image() == 1:
                time.sleep(2)           
            time.sleep(2)
            pyautogui.write(kod)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)
            nudes = kod
        
def get_token():
    global token
    if(os.path.isfile('discord_token.txt') == True):
        file = open("discord_token.txt")
        token = file.read()
        file.close()
    else:
        print("Nie ma pliku discord_token.txt lub wystompił problem z jego odczytaniem")

if __name__ == '__main__':
    get_token()
    time.sleep(2)
    wiadomosc_dioscrd('868574854536888401')
    

