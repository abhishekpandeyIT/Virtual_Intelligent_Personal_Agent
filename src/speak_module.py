from gtts import gTTS
from playsound import playsound
import os



def speak(text):
    tts=gTTS(text)
    tts.save('speech.mp3')
    playsound('speech.mp3',True)
    os.remove('speech.mp3')
