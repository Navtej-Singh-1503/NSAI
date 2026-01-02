'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

01/01/2026

Version - 0.5.3

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
from DATA import SYSTEM_PROMPT
import json
import os

MEMORY_FILE = "memory.json"

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


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


chat_history = load_memory()

if not chat_history:
    chat_history = [
        {
            "role": "model",
            "parts": [{"text": SYSTEM_PROMPT}]
        }
    ]


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

    if user.lower() == "exit":
        print(RED + "AI: Bye 👋" + RESET)
        engine.say("Goodbye")
        engine.runAndWait()
        break

    chat_history.append({
        "role": "user",
        "parts": [{"text": user}]
    })

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=chat_history
        )

        ai_text = response.text.strip()

        chat_history.append({
            "role": "model",
            "parts": [{"text": ai_text}]
        })
        save_memory(chat_history)

        print(PURPLE + "AI: " + ai_text + RESET)
        speak(ai_text)

    except Exception as e:
        if "429" in str(e):
            print("AI NEED SOME REST.")
            print("TRY AGAIN AFTER 12:00am")
            print("STAY UPDAPED IT WILL FIX SOON...")

        elif "400" in str(e):
            print("AI: Invalid request. Something in your message format is wrong.")
            print("Check your system prompt or input.")

        elif "401" in str(e):
            print("AI: Authentication failed. API key is invalid or missing.")

        elif "403" in str(e):
            print("AI: Permission denied. Your plan may not allow this model.")

        elif "404" in str(e):
            print("AI: Requested model or resource not found. Check the model ID.")

        elif "500" in str(e):
            print("AI: Server error. The API's had a problem. Try again later.")

        elif "502" or "503" in str(e):
            print("AI: Server is temporarily unavailable. Please wait a few seconds and retry.")

        elif "SSL" in e:
            print("AI: Network/SSL problem. Check your internet, firewall, or VPN.")

        elif "Erron" in e:
            print("AI: Network error. Check your internet connection and DNS.")
        else:

            print(RED + "[!] Error:" + RESET, e)
