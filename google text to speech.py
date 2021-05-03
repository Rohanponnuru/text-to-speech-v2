from gtts import gTTS
import os 

text = " python is the most easiest programing language "

language = "en-us"
roh = gTTS( text = text , lang = language , slow = False)
roh.save("play.mp3")
os.system(" start play.mp3")