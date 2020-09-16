import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import smtplib

print("initializing jarvis")
MASTER = "Jayson"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak("Good Morning "+MASTER)   
    elif hour>=12 and hour<18:
        speak("Good Afternoon "+MASTER)
    else:
        speak("Good Evening "+MASTER)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-us')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that Again please")
        query=""
    return query



speak("Initializing Command....")
speak(f"Hi {MASTER} Im Jarvis your AI assistant...")
wishMe()

while(True):

    
    query = takeCommand()

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak(results)

    elif 'open youtube' in query.lower():
        speak(f"wait {MASTER} openning youtube..")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif 'open google' in query.lower():
        speak(f"wait {MASTER} openning google..")
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        speak(f"wait {MASTER} i playing music for you the best as I can..")
        songs_dir = "C:\\Users\\Jayson\\Desktop\\music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[8]))

    elif 'the time' in query.lower():
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strtime}")

    elif 'open code' in query.lower():
        code_path = "C:\\Users\Jayson\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'stop program' in query.lower():
        break

