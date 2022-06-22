import pyttsx3
import wikipedia
import os
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    

# simple function to recognise speech from user
def takecommand():
    #it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('User Said : ' , query)

    except Exception as e:
        print('exception : ',e)

        speak("Sorry, I didn't hear that, Say that again Please")
        return "None"
    return query

def takename(usefulquery):
    words = usefulquery.split()
    return(words[3])
    



if __name__ == "__main__" :

    while True :
        usefulquery = takecommand().lower() # whatever user says will be stored in this variable
        
        if 'hello' in usefulquery :
            print()
            speak("hello" + takename(usefulquery) + "I am DEV what can i do for you")
        elif 'who is' in usefulquery:
            speak("Searching..")
            usefulquery = usefulquery.replace("","")
            results = wikipedia.summary(usefulquery,sentences = 1)
            print(results)
            speak(results)
        elif 'what is' in usefulquery:
            speak("Searching..")
            usefulquery = usefulquery.replace("","")
            results = wikipedia.summary(usefulquery,sentences = 1)
            print(results)
            speak(results)
        elif "open youtube" in usefulquery:
            codepath = "C://Users//devan//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Brave Apps//YouTube.lnk"
            os.startfile(codepath)
            break
        elif "open whatsapp" in usefulquery:
            codepath = "C://Program Files//WindowsApps//5319275A.WhatsAppDesktop_2.2144.11.0_x64__cv1g1gvanyjgm//app//WhatsApp.exe"
            os.startfile(codepath)
            break
        elif "play music" in usefulquery:
            codepath = "C://Users//devan//Desktop//Resso.lnk"
            os.startfile(codepath)
            break
        elif 'exit' in usefulquery: 
            print("okay call me again whenever you need")
            speak("okay call me again whenever you need")
            break

