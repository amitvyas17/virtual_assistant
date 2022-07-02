import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print ("Initialiazing Zin")
MASTER ="Amit"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

#peak('amit is good')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
        speak ("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak ("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    speak(" I am zin. How may i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         audio= r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, Language ='en-in')
        print (f"user said:  {query}\n")

    except Exception as e:
        print("Please say that again")
        query = None
    return query

def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vyasamit1717@gmail.com', 'amit8619317460')
    server.sendmail("17vyasamit@gmail.com", to, content)
    server.close()
speak("Initializing Zin....")
wishMe()
query = takeCommand()


if 'wikipedia' in query.lower():
    speak('searching Wikipedia...')
    query = query.replace("wikipedia","")
    results =wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url ="youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir =os.listdir("C:\\Users\\Amit Vyas\\Downloads\\Music")
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir , songs[0]))
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")

elif 'email to Amit' in query.lower():
    try:
        speak("What should i send")
        content = takeCommand()
        to = "17vyasamit@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent sucessfully")
    except Exception as e:
        print(e)