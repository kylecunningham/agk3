from .. import steel
class tts_voice(object):
	def __init__(self):
#Initializes the Steel TTS library to use the SAPI5 engine.

		self.engine=steel.SAPI5()

	def set_rate(self, rate):
#set the tts rate

		self.engine.set("rate",rate)

	def speak(self,text,interrupt=False):
#Make the TTS voice speak. Interrupt will make the tts voice stop speaking before the next string starts.

		if interrupt==True:
			self.engine.stop()

		self.engine.speak(text)