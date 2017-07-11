#This example will teach you how to speak through the SAPI5 TTS Engine.
#we import time so we can sleep
import time
#import the SAPI speaker
from AGK.speech import SAPI
#create a SAPI5 voice instance.
voice=SAPI.tts_voice()
#speak something
voice.speak("This is a test.")
#sleep
time.sleep(3)