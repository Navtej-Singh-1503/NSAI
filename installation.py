from brand import intro
import os
import time

print(intro)
time.sleep(1)
print("--NEED TO INSTALL SOME LINUX PACKAGES AND PYTHON3 PACKAGES--")
print("Installation will be starting in 5 seconds ")

time.sleep(5)

os.system("sudo apt update")
os.system("sudo apt install espeak espeak-ng ffmpeg libespeak1 alsa-utils -y")
os.system("pip install pyttsx3 --break-system-packages")
os.system("pip install google-generativeai --break-system-packages")
os.system("pip install google-genai")

print("DONE........... NOW NOW YOU CAN START RUNNING ai.py")
print("Need Gemini API Key to run ai.py")
print("If you don't have you can get it on ")
key = input("Enter you Google gemini API Key>> ")

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



