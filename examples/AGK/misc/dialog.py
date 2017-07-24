from attr import attrs, attrib, Factory
from ..speech import auto, SAPI
from ..mainframe import keyboard
from ..audio import sound
import pygame

@attrs
class dialog(object):
	text = attrib()
	popup_sound = attrib(default=Factory(str))
	SAPI = attrib(default=Factory(bool))
	
	def __attrs_post_init__(self):
		self.display()

	def display(self):
		if self.popup_sound != "":
			handle = sound.sound()
			handle.load(self.popup_sound)
			handle.play()
		self.speak(self.text + " To repeat, press R. To dismiss, press enter.")
		while 1:
			for evt in pygame.event.get():
				if evt.type == pygame.KEYDOWN:
					if evt.key==pygame.K_r:
						self.speak(self.text)
					if evt.key == pygame.K_RETURN:
						return 1

	def speak(self, text):
		if self.SAPI==True:
			SAPI.speak(text)
		else:
			auto.speak(text)

