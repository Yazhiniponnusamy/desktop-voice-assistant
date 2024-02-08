import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pyautogui
from pynput.keyboard import Controller as key_controller
from pynput.keyboard import Key


from bs4 import BeautifulSoup
import requests
import json
import time
import smtplib
from gtts import gTTS

from requests import Response

from urllib.request import urlopen
from googletrans import Translator
from GoogleNews import GoogleNews

googlenews=GoogleNews()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
keyboard = key_controller()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am josephite. I am your Assistant. How can i help you?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")


        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

def search():
    r=sr.Recognizer()

    with sr.Microphone() as src:
        print("what do you want to search? ")
        speak("what do you want to search")
        audio = r.listen(src)
        try:
            text = r.recognize_google(audio)
            url = 'https://www.google.co.in/search?q='
            search_url = url + text
            webbrowser.open(search_url)
        except:
            print("can't recognize")
    def note(query):
        date = datetime.datetime.now()
    file_name = str(datetime).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        '''f.write(text)'''
    sublime = "C:\\Program Files\\Sublime Text\\sublime_text.exe"
    subprocess.Popen([sublime, file_name])

def notepad():
    pyautogui.press('win', interval=0.2)
    pyautogui.typewriter('notepad', interval=0.1)
    pyautogui.press('enter', interval=0.2)
def speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening... ")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("recognizing...")
            query=r.recognize_google(audio,language='en-in')
            if 'save' in query:
                pyautogui.hotkey('ctrl', 's')
                time.sleep(2)
                FILE_NAME="C:\\Users\\HP\\Desktop\\OpenCV\\sample.txt"

                pyautogui.hotkey('enter')
            else:
               query= r.recognize_google(audio, language='en-in')
            pyautogui.typewrite(query)
        except Exception as e:
            print("error")

def eng_tam():
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        audio = r.listen(source)
        print("Done!")
    text = r.recognize_google(audio, language='en-in')
    translate_text = translator.translate(text, dest='ta')
    print(translate_text.text)
def tam_eng():
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        audio = r.listen(source)
        print("Done!")
    text = r.recognize_google(audio, language='ta')
    translate_text = translator.translate(text, dest='en')
    print(translate_text.text)
def tam_hi():
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        audio = r.listen(source)
        print("Done!")
    text = r.recognize_google(audio, language='ta')
    translate_text = translator.translate(text, dest='hi')
    print(translate_text.text)
def en_hi():
    translator = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something...")
        audio = r.listen(source)
        print("Done!")
    text = r.recognize_google(audio, language='en')
    translate_text = translator.translate(text, dest='hi')
    print(translate_text.text)

def tamil():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    text=r.recognize_google(audio,language='ta')
    print(text)

def weather():
    api_key = "41c177fb938536e752e44625b4b70425"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    print("Tell the city name ..........")
    speak("tell the city name you want to get an weather report")
    city_name = takeCommand()
   #print("The city name is : +city_name ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        fahrenheit = current_temperature * 9 / 5 - 459.67
    celsius = current_temperature - 273.15
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n Temperature in fahrenheit = " +
          str(fahrenheit) +
          "\n Temperature in celsius = " +
          str(celsius) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))

    speak(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n Temperature in fahrenheit = " +
          str(fahrenheit) +
          "\n Temperature in celsius = " +
          str(celsius) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))


if __name__ == "__main__":
    wishMe()

    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'temperature' in query:
            weather()

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open notepad' in query:
            codepath = "C:\\Windows\\notepad.exe"
            os.startfile(codepath)
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)
        elif 'open chrome' in query:
            codepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Google Chrome"
            os.startfile(codepath)
        elif 'google' in query:
            search()
        elif 'find my location' in query:
            url = "http://ipinfo.io/json"
            response = urlopen(url)
            data = json.load(response)
            print(data)
        elif 'make a note' in query:
            notepad()
            while True:
                speech()
        elif 'translate to tamil' in query:
            eng_tam()
        elif 'translate to hindi' in query:
            en_hi()
        elif 'translate' in query:
            tamil()
        elif 'translate to english' in query:
            tam_eng()
        elif 'translate to hindi' in query:
            tam_hi()
        elif 'headlines' in query:
            engine.say("getting news for you")
            engine.runAndWait()
            googlenews.get_news('Today news')
            googlenews.result()
            a = googlenews.gettext()
            a = print(*a[1:5], sep=',')
            print(a)
            # speak(a)
        elif 'stop' in query:
            pyautogui.hotkey('ctrl', 'f2')

        else:
            speak("sorry,I couldn't recognize your voice")
