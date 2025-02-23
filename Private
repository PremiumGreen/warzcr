from pyexpat.errors import messages
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

def windowtitle(a):
    os.system(f"title {a}")
windowtitle("N̴̗̜̜̼̤̈́͂̑͋͋̈̌͆͋̓̉̑͝͝ģ̴̛̱̫͕͎̻̩͚̺͖̣̖̠̘̝̀̃͆̽̆̈́̈́̅̈͒̾̈́̇̐͒̈̚͝͝ͅơ̴͔̂͊̔̆͐͛̈́͂̌͗̂̇̊͋͠͠͠͝ͅc̸̢̫̓̉H̸̨̢͕̬̺͔͔̟̗̐̐̍̊̿͂̾̋̈́͂́̂̇̈̑͘̚͜͜͠ű̵̧̧̙̼͖̺͈̲̭͉͕̖̬̪̝͖̟̭͔̱̤̠̳̥̃̀̍͑͗͛̈̄̚͜ͅͅͅy̴̭̳̗͎̣̳̗͍̠̲̘̎̌͛̅́̊͝͠")

init(autoreset=True)

def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

def update_keys():
    try:
        response = requests.get("https://raw.githubusercontent.com/PremiumGreen/SISEMET/refs/heads/main/key.json")  # Thay đổi URL đến tệp JSON của bạn
        response.raise_for_status()
        keys_data = response.json()["keys"]

        for key, info in keys_data.items():
            if info["type"] == "trial":
                expiry = datetime.fromisoformat(info["expiry"])
                valid_keys[hash_key(key)] = {"type": "trial", "expiry": expiry, "used": info.get("used", False)}
            else:
                valid_keys[hash_key(key)] = {"type": "permanent", "used": False}
    except Exception as e:
       print(f"Lỗi khi cập nhật khóa: {e}")

valid_keys = {}
update_keys() 

def validate_key(user_key: str) -> bool:
    hashed_user_key = hash_key(user_key)
    key_info = valid_keys.get(hashed_user_key)

    if key_info:
        if key_info["type"] == "permanent":
            return True
        elif key_info["type"] == "trial":
            if datetime.now() < key_info["expiry"]:
                if not key_info["used"]: 
                    key_info["used"] = True 
                    return True
                else:
                    messagebox.showerror("Đã có người khác dùng key")
                    messagebox.showerror("The key has been used by another user")
                    print(Fore.RED + "Khóa trải nghiệm đã được sử dụng.")
                    return False
            else:
                messagebox.showerror("Khóa trải nghiệm đã hết hạn")
                messagebox.showerror("The trial key has expired")
                print(Fore.RED + "Khóa trải nghiệm đã hết hạn.")
                return False
    else:
        messagebox.showerror("Khóa không hợp lệ")
        messagebox.showerror("Invalid key")
        print(Fore.RED + "Khóa không hợp lệ.")
        return False


def main():
    os.system('cls')
    print(Fore.BLUE + "Chào Em Yêu")
    while True:
        os.system('cls')
        user_key = input(Fore.YELLOW + "Vui Lòng Nhập Key: ")
        
        if validate_key(user_key):
            print("Giỏi Quá, Key Đã Đúng.")
            break  
        else:
            print(Fore.GREEN + "Sai Mã Key, Vui Lòng Liên Hệ tele Nghdz để lấy key mới")
            input(Fore.RED + "Key Sai, Vui Lòng Ấn Enter Để Nhập Lại Key ")

if __name__ == "__main__":
    main()
os.system('cls')


banner = f"""
    
               _  __                __ __         
              / |/ /__ ____  ____  / // /_ ____ __
             /    / _ `/ _ \/ __/ / _  / // / // /
            /_/|_/\_, /\___/\__/ /_//_/\_,_/\_, / 
                 /___/                     /___/
{Fore.RED}-----------------------
{Fore.BLUE}Creator: N̶͕̆g̸͕͗̐o̷͎̎c̴͔̹͐̔ ̶̻̀H̶̹̐u̷̖͠y̴͈̗̿̿
{Fore.RED}-----------------------
{Fore.BLUE}Contact: https://t.me/nghdz
{Fore.RED}Đây chính là tool spam tự lập(for all chat)

"""
print(banner)
messages = input("Nhập tin nhắn (cách nhau bằng dấu ','): ").split(',')
loop_forever = input("Bạn có muốn spam liên tục không? (Y/N): ").strip().lower()

if loop_forever == 'y' or loop_forever == 'Y':
    times = float('inf')
else:
    times = int(input("Nhập số lần gửi tin nhắn: "))
print("Bạn có 5 giây để chuyển sang cửa sổ Zalo...")
time.sleep(5)
count = 0
while count < times:
    for msg in messages:
        pyperclip.copy(str(msg).strip())
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.1)
    count += 1

messagebox.showerror("SPAM HOÀN TẤT")



