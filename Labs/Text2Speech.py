from gtts import gTTS
import os


langauge = 'EN'             #Sets the language
yourText = "Hello Daddy Senpai."

output = gTTS(text=yourText, lang=langauge, slow=False) 
#gTTS expects this naming scheme so I am passing it my two variables
#gTTS has two speeds of playback: Fast and Slow. I want Fast.
