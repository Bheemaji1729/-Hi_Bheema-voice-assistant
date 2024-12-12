import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki


listener = sr.Recognizer()
speaker = pyttsx3.init()
""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
speaker.setProperty('rate', 130)     # setting up new voice rate
"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def speak(text):
    speaker.say("yeah bro" + text)
    speaker.runAndWait()
def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

va_name = "chintu"
speak_ex("hello bro iam your " + va_name + "how can i help you, tell me bro ")

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening... ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + " ","")
                #print(command)
                #speak(command)
    except:
        print("check your Microphone")  
    return command
while True:
  user_command = take_command()  
  if "close" in user_command:
      print("see you again bro. I will be there when ever you call me.")
      speak_ex(" ok bro see you again. I will be there when ever you call me.")
      break
  elif "time" in user_command:
      current_time = dt.datetime.now().strftime("%I:%M %p")
      print(current_time)
      speak(current_time)
  elif "play" in user_command:
      user_command = user_command.replace("play ","")
      print("playing " + user_command)
      speak("playing " + user_command +  " enjoy bruhh ")
      pk.playonyt(user_command)
      break
  elif "search for" in user_command or "google" in user_command:
      user_command = user_command.replace("search for ", "")
      user_command = user_command.replace("google ", "")
      #print("searching for "+ user_command)
      speak("searching for "+ user_command)
      pk.search(user_command)
      break
  elif "who is" in user_command or "what is" in user_command:
      user_command = user_command.replace("who is ", "")
      info = wiki.summary(user_command, 2)
      print(info)
      speak(info)
  elif "who are you" in user_command:
      speak_ex(" hai bro iam your personal assistant named as chintu ")
  else:
    speak_ex("please say it again bro.")

     
 
