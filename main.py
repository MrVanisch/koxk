import pyautogui as pt
import pyautogui
import time 
import requests
import json
import webbrowser
import os
import datetime

cookies = ""
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
            print("Nie znaleziono elementu.")
            return 1

def wiadomosc_dioscrd(idkanalu,cookies):
    global nudes
    global token
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
            url = "https://key-drop.com/pl/Api/activation_code"
            payload = json.dumps({
            "promoCode": kod,
            "recaptcha": None
            })
            headers = {
             'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'content-type': 'application/json',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'host': 'key-drop.com',
            'Cookie': cookies
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            kox = json.loads(response.text)
            print("Rezultat:",kox['status'])
            nudes = kod
        time.sleep(10)

def cookieszmiana():
    global cookies
    start = Clicker('start.png', speed=.8)
    potiwerdzenie = Clicker('potiwerdzenie.png', speed=.8)
    time.sleep(5)
    if(os.path.isfile('cookies.txt') == True):
        os.remove('cookies.txt')
    webbrowser.open('https://key-drop.com/pl/')
    time.sleep(5)
    while  start.nav_to_image() ==1:
        time.sleep(2)
    while potiwerdzenie.nav_to_image() ==1:
        time.sleep(2)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    file = open("cookies.txt")
    cookies = file.read()
    file.close()


def get_token():
    global token
    if(os.path.isfile('cookies.txt') == True):
        file = open("discord_token.txt")
        token = file.read()
        file.close()
    else:
        print("Nie ma pliku discord_token.txt lub wystompił problem z jego odczytaniem")

if __name__ == '__main__':
    cookieszmiana()
    time.sleep(2)
    get_token()
    time.sleep(2)
    wiadomosc_dioscrd('868574854536888401',cookies)
    

