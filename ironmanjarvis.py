import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pywhatkit as pyt
from plyer import notification
import googlesearch as gs   
import webbrowser as wb
import bs4 as df
import re 
import requests
import subprocess
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import pywhatkit as pykt 
import googlesearch as gs   
import webbrowser as wb


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yearsofmusic@gmailcom' , 'Ineedgoldpass$1')
    server.sendmail('yearsofmusic@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=3 and hour <12:
        speak("Good Morning!")
    elif hour >=12 and hour <16:
        speak("Good Afternoon!")
    elif hour >=16 and hour <20:
        speak("Good Evening!")
    elif hour >=20 and hour <=3:
        speak("Good Night!")
    speak("How can I help you?")

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



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand() . lower()
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry I am unable to find this")
        
        elif 'youtube' in query:
            try:
                speak('Searching Youtube...')
                query = query.replace("Youtube", "")
                music_name = query
                query_string = urllib.parse.urlencode({"search_query": music_name})
                formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
                search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
                clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
                clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

                pykt.playonyt(clip2)

            except Exception as e:
                print(e)
                speak("Sorry I am unable to find this")
        
                  
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        
        elif 'stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            
      
        
        elif 'google' in query:
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")

            query = query = query.replace("Google", "")

            for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(j)
       
             
        elif 'exit' in query:
            speak("Bye Bye")
            sys.exit()