import pyttsx3
import speech_recognition as sr
import datetime
#import wikipedia
import webbrowser
import os
import setuptools
#from gtts import gTTS


# Taking voice from my system

#engine = pyttsx3.init("sapi5")  #initialize the library by init() and give 'sapi5' in order to access the speech property, it is a parameter
#engine.say("hello from mac")
#engine.runAndWait()

engine = pyttsx3.init() 
#engine = "This text will be spoken by Google's TTS."
#tts = gTTS(text=engine, lang='en')  # Choose your desired language

voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty('rate',150)

# speak function

def speak(text):
    ''''This function takes text nd returns voice 
    
    Args: 
       text (_type): string
    '''
    engine.say(text)
    engine.runAndWait()

speak("Hello I am a programmer, how are you?")


# speech recognition function
def takeCommand():
    '''
    this function will recognize voice & return text   
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening successfully...") 
        r.pause_threshold = 1 # in order to recognize the voice correctly
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language= 'en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return None
        return query
    

# takeCommand()
text = takeCommand()
speak(text)

# The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening ")

    speak("I am Keerthi")




if __name__ == "__main__":

    wish_me()

    while True:
        query =  takeCommand().lower()
        print(query)
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia',"")
           #print(query)
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "goodbye" in query:
            speak("bye bye")
            exit()