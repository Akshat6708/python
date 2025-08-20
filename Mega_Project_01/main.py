import speech_recognition as sr
import pyttsx3
import requests
import wikipedia
import datetime
import pywhatkit
import webbrowser
import os
import pyautogui
from pathlib import Path

# ====== TTS / STT ======
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio)
            print("👉 You said:", command)
            return command.lower().strip()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech service is unavailable right now.")
        except Exception:
            speak("Something went wrong with listening.")
        return ""

def confirm_action(prompt="Are you sure? Say yes or no."):
    speak(prompt)
    ans = listen()
    return ans in ("yes", "yeah", "yup", "ok", "okay", "confirm", "sure")

# ====== WEATHER ======
def get_weather(city="London"):
    api_key = "PUT_YOUR_OPENWEATHERMAP_KEY"
    if api_key == "PUT_YOUR_OPENWEATHERMAP_KEY":
        return "Weather API key is missing. Please add it first."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        resp = requests.get(url, timeout=8).json()
        if resp.get("cod") == 200:
            temp = resp["main"]["temp"]
            desc = resp["weather"][0]["description"]
            return f"The temperature in {city} is {temp} degrees Celsius with {desc}."
        return "I couldn't fetch the weather right now."
    except Exception:
        return "Network error while fetching the weather."

# ====== APP LAUNCHER ======
def open_app(app_name):
    try:
        if "notepad" in app_name:
            os.system("notepad")
        elif "calculator" in app_name:
            os.system("calc")
        elif "chrome" in app_name:
            os.system("start chrome")
        elif "vs code" in app_name or "visual studio code" in app_name or "code" in app_name:
            os.system("code")
        else:
            speak("Sorry, I don't know how to open " + app_name)
    except Exception:
        speak("Something went wrong opening " + app_name)

# ====== SYSTEM CONTROLS ======
def lock_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    speak("Locking your computer.")

def shutdown_pc():
    if confirm_action("This will shut down your PC. Do you want to proceed?"):
        speak("Shutting down now.")
        os.system("shutdown /s /t 0")

def restart_pc():
    if confirm_action("This will restart your PC. Do you want to proceed?"):
        speak("Restarting now.")
        os.system("shutdown /r /t 0")

def take_screenshot():
    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filepath = os.path.join(desktop, f"screenshot_{ts}.png")
        image = pyautogui.screenshot()
        image.save(filepath)
        speak(f"Screenshot saved to Desktop as screenshot underscore {ts}.")
    except Exception:
        speak("I couldn't take the screenshot.")

# ====== MAIN LOOP ======
def voice_assistant():
    speak("Hello, I am your smart assistant. How can I help you?")
    while True:
        command = listen()
        if not command:
            continue

        if "hello" in command:
            speak("Hello! How can I assist you?")
        elif "your name" in command:
            speak("I am your Python assistant.")
        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            break

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")

        elif "weather" in command:
            speak("Which city?")
            city = listen()
            if city:
                speak(get_weather(city))

        elif "wikipedia" in command:
            speak("What should I search on Wikipedia?")
            topic = listen()
            if topic:
                try:
                    summary = wikipedia.summary(topic, sentences=2)
                    speak(summary)
                except wikipedia.exceptions.DisambiguationError:
                    speak("That term has multiple meanings, please be more specific.")
                except:
                    speak("Sorry, I couldn't find that on Wikipedia.")

        elif "google" in command:
            speak("What do you want me to search on Google?")
            query = listen()
            if query:
                try:
                    pywhatkit.search(query)
                    speak(f"Searching Google for {query}")
                except:
                    speak("Couldn't perform the Google search.")

        elif "youtube" in command or "play on youtube" in command:
            speak("What should I play on YouTube?")
            video = listen()
            if video:
                try:
                    pywhatkit.playonyt(video)
                    speak(f"Playing {video} on YouTube")
                except:
                    speak("Couldn't play the video on YouTube.")

        elif "open website" in command:
            speak("Which website?")
            site = listen()
            if site:
                site = site.replace(" dot ", ".")
                url = f"https://{site}"
                speak(f"Opening {url}")
                webbrowser.open(url)

        elif command.startswith("open "):
            app = command.replace("open", "", 1).strip()
            if app:
                open_app(app)

        elif "lock" in command:
            lock_pc()
        elif "shutdown" in command:
            shutdown_pc()
        elif "restart" in command:
            restart_pc()
        elif "screenshot" in command:
            take_screenshot()

        else:
            speak("You said " + command)

if _name_ == "_main_":
    voice_assistant()