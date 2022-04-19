'''Making Jarvis to do addition'''
import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',190)
engine.setProperty('volume',1.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
   hour=int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning sir,let's do some addition")
   elif hour>=12 and hour<16:
      speak("Good Afternoon sir, let's do some addition")
   else :speak("Good evening sir,let's do some addition")

def command():
   r=sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening sir")
      r.pause_threshold=1
      audio=r.listen(source)
   try:
      print("Recognizing...")
      query=r.recognize_google(audio,language='en-in')
      print(f"User said:{query}\n")
   except Exception as e:
      print(e)
      print("Say that again please....")
      return "None"
   return query

wishme()
query=command().lower()
speak("Tell your first value sir")
query=command().lower()
a=query

#a=int(input("Enter your 1st value sir"))
print(a)
speak("Tell your second value sir")
query=command().lower()
b=(query)
#b=int(input("Enter your second value sir"))
print(b)
c=int(a)+int(b)
speak(f'your result is {c}')
print(f'Your result is {c} sir')


