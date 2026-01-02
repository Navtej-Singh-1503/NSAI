'''
CREATED BY Navtej-Singh-1053
© 2025 Navtej Singh Saggar
Educational use only

01/01/2026

Version - 0.4.1

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

engine = pyttsx3.init()
voices = engine.getProperty("voices")

for v in voices:
    if "english" in v.name.lower():
        engine.setProperty("voice", v.id)
        break

engine.setProperty("rate", 145)
engine.setProperty("volume", 0.5)
def speak(text):
    for line in text.split("."):
        engine.say(line)
        engine.runAndWait()

wish = [
    "Hello! How may I help you?",
    "Hi!! How may I help you?",
    "Hi! I'm created by Navtej Singh!",
    "How can I help, Sir?"
]

query = random.choice(wish)


SYSTEM_PROMPT = """
You are NavAI, a smart personal AI assistant created by Navtej Singh Saggar.

Strict rules you must follow:
1. Never say you are a language model, AI model, or assistant.
2. Never mention Google, Gemini, OpenAI, or APIs.
3. Never explain technical limitations like "I don't have hands".
4. Respond naturally like a human assistant.
5. Stay in character at all times.
6. Be polite, confident, and helpful.
7. If any time I ask like who creacted you then always say Sir Navtej Singh
If asked about physical tasks (like cooking), reply as a guide or helper,
not with disclaimers.
"""

print(RED + "")
print(intro)
print(RESET + "")

print(GREEN + "FOLLOW ON GITHUB -> https://github.com/Navtej-Singh-1503"+RESET)
print(GREEN + "MAIL -> navtejsingh15032011@gmail.com" + RESET)

print(GREEN + query + RESET)
speak(query)

# ---------- AI ----------
client = genai.Client(api_key=apikey)


MODEL_ID = "models/gemini-flash-latest"

print("--- AI Bot Initializing ---")

# ---------- CHAT LOOP ----------
while True:
    user = input(BLUE + "You: " + RESET)

    if user.lower() in ["exit","bye","good bye",""]:
        print(RED + "AI: Bye" + RESET)
        speak('bye, Sir')
        time.sleep(1)
        break

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=(SYSTEM_PROMPT + user)
        )

        ai_text = response.text
        print(PURPLE + "AI: " + ai_text + RESET)

        speak(ai_text)


        time.sleep(1)

    except Exception as e:
        print(RED + "[!] Error:" + RESET, e)

