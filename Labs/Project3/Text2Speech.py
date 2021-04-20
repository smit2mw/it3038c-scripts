from gtts import gTTS
import os


langauge = 'EN'             #Sets the language
yourText = input("Enter your text:  ")

output = gTTS(text=yourText, lang=langauge, slow=False) 
#gTTS expects this naming scheme so I am passing it my two variables
#gTTS has two speeds of playback: Fast and Slow. I want Fast.

output.save("Text2Speech.mp3") #Saves the output as mp3 file on your computer

os.system("start Text2Speech.mp3") #Plays the afore mentioned audio file