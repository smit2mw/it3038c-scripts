from gtts import gTTS   #Google's Text to Speech API
import os


langauge = 'en' 
#Sets the language

yourText = input("Enter your text:  ")
#User enters the Text they'd like to hear

output = gTTS(text=yourText, lang=langauge, slow=False) 
#gTTS expects this naming scheme so I am passing it my two variables
#gTTS has two speeds of playback: Fast and Slow. I want Fast.

output.save("Text2Speech.mp3") 
#Saves the output as mp3 file on your computer
#More specifically it will save it to the folder in which this file resides

os.system("start Text2Speech.mp3") 
#Plays the afore mentioned audio file
#If you are on a Windows Computer this will open Groove to play the audio file