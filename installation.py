'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

01/01/2026

Version - 3.1.3

mail - navtejsingh15032011@gmail.com

'''

from brand import intro
import os
import time

RED = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0m"
os.system('clear')

print(RED + intro)
time.sleep(1)
print(GREEN+"--NEED TO INSTALL SOME LINUX PACKAGES AND PYTHON3 PACKAGES--")
print("Installation will be starting in 5 seconds "+RESET)

time.sleep(5)

os.system("sudo apt update")
os.system("sudo apt install espeak espeak-ng ffmpeg libespeak1 alsa-utils espeak-ng-data -y")
os.system("pip install pyttsx3 --break-system-packages")
os.system("pip install google-generativeai --break-system-packages")
os.system("pip install google-genai --break-system-packages")

print(GREEN+"DONE........... NOW NOW YOU CAN START RUNNING ai.py")
print("Need Gemini API Key to run ai.py")
print("If you don't have you can get it on https://aistudio.google.com/api-keys")
key = input("Enter you Google gemini API Key>> ")

with open("api.py", "w") as f:
    f.write('apikey = "'+key+'"')

print("api.py file created successfully!"+RESET)

user = input("NEED MORE GITHUB TOOLS?    [Yes/No]")
if user.lower() in ["yes", "y"]:
	os.system("git clone https://github.com/Navtej-Singh-1503/Android-viruses")
	os.system("git clone https://github.com/Navtej-Singh-1503/Tiny-Platformer-Game")
	print("DONE... MORE TOOLS ARE INSTALLED THANKS!")
elif user.lower() in ["no", "n"]:
	print("OKK!!")
else:
	print("invaild input")
	os.system("installation.py")



