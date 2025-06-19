import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=.6
        audio=r.listen(source)
        try:
            
            query=r.recognize_google(audio,language='en-in')
            print(f"You said: {query}\n")
            return query
        except Exception as e:
            return "Some error occurred, please try again."

if __name__ == "__main__":
    say("Hello, I am Jarvis. How can I assist you today?")
    while True:
        print("Listening for commands...")
        query= takeCommand()
        sites=[["Youtube", "https://www.youtube.com/"],["wikipedia", "https://www.wikipedia.com/"],["google", "https://www.google.com/"],["amazon", "https://www.amazon.com/"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                
                say(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])
        if "open music"in query:
            say("Opening Music Sir")
            musicpath="E:\Outside Work\ghum.mp3"
            os.startfile(musicpath)
        if "the time" in query:
            strftime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strftime}")
        if "Open ppt".lower() in query.lower():
            say("Opening PowerPoint Sir")
            pptpath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(pptpath)

