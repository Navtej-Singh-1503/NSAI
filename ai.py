'''
CREATED BY Navtej-Singh-1053
© 2025 Navtej Singh Saggar
Educational use only

01/01/2026

Version - 0.3.4

mail - navtejsingh15032011@gmail.com

'''
#This is the main script

from google import genai
import time
import random
import pyttsx3
from brand import intro
import os
from api import apikey

RED = "\033[1;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

os.system("clear")

engine = pyttsx3.init("espeak")
engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

wish = [
    "Hello! How may I help you?",
    "Hi!! How may I help you?",
    "Hi! I'm created by Navtej Singh!",
    "How can I help, Sir?"
]

query = random.choice(wish)

print(RED + "")
intro()
print(RESET + "")

print(GREEN + "FOLLOW ON GITHUB -> https://github.com/Navtej-Singh-1503"+RESET)
print(GREEN + "MAIL -> navtejsingh15032011@gmail.com" + RESET)

print(GREEN + query + RESET)
engine.say(query)
engine.runAndWait()  

# ---------- AI ----------
client = genai.Client(api_key=apikey)


MODEL_ID = "models/gemini-flash-latest"

engine.say("AI Bot Initializing")
engine.runAndWait()
print("--- AI Bot Initializing ---")

# ---------- CHAT LOOP ----------
while True:
    user = input(BLUE + "You: " + RESET)

    if user.lower() == "exit":
        print(RED + "AI: Bye 👋" + RESET)
        engine.say("Goodbye")
        engine.runAndWait()
        break

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user
        )

        ai_text = response.text
        print(PURPLE + "AI: " + ai_text + RESET)

        engine.say(ai_text)
        engine.runAndWait() 

        time.sleep(1)

    except Exception as e:
        print(RED + "[!] Error:" + RESET, e)

