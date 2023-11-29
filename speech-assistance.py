import speech_recognition as sr
import webbrowser
from time import ctime
import pyttsx3

r = sr.Recognizer()
def record_audio( ask = False):
   with sr.Microphone() as source:
    if ask:
        speak(ask)
    audio = r.listen(source)
    voice_data = ''
    try:
       voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
       speak ("sorry i cannot undersatsnd, can you say it again ")
    except sr.RequestError:
       speak ("sorry i can't find the result , please try again later ")
    return voice_data

def speak (answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()
    print(answer)

def answers (voice_data):
  if "name" in voice_data:
   speak ("my name is Tom")
  if "time" in voice_data:
     speak (ctime())
  if "jerry" in voice_data:
   search = record_audio("what you want to google ?")
   url = 'https://google.com/search?q=' + search
   webbrowser.open(url)
   speak ("this is the data i found " + search)
  if "thankyou" in voice_data:
      speak ("thankyou")
      exit()


speak ("How can I help you ")
while 1:
    voice_data = record_audio()
    answers (voice_data)



