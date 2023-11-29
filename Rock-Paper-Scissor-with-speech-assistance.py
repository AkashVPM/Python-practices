import speech_recognition as sr
import pyttsx3
import random

# for speech recognition
r = sr.Recognizer()
def record_audio( ask = False, timeout = 10):
   with sr.Microphone() as source:
        if ask:
            speak(ask)
        voice_data = ''
        try:
           audio = r.listen(source, timeout=timeout)
           voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
           speak ("sorry i cannot undersatsnd, can you say it again ")
        except sr.RequestError:
           speak ("sorry i can't find the result , please try again")
        return voice_data.lower()

# for read the result
def speak (answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()
    print(answer)


# getting output from computer 
def player (play):
    option = ["rock", "paper", "scissor"]
    computer_choice = random.choice(option)
    speak(f"you chose {play} and computer chose {computer_choice}")

# win or loose conditions 
    if play == computer_choice:
        speak("so, the match is a tie")
    elif (play == "rock" and computer_choice == "paper") or (play == "scissor" and computer_choice == "rock") or (play == "paper" and computer_choice == "scissor"):
        speak("you loose")
    else:
        speak("you win")

# getting the input from the player in loop 

while True:
    player_choice = record_audio("please Choose rock, paper, or scissor")
    options = ["rock", "paper", "scissor"]

    if player_choice in options:
        player(player_choice)
    if "thanks" in player_choice:
        speak ("you welcome ")
        exit()
    if player_choice not in options:
        speak("sorry")
