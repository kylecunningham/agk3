from ..speech import auto, SAPI
from ..mainframe import keyboard
import pygame

class dialog(object):
	def __init__(self, text, SAPI=False):
		self.text = text
		self.SAPI=SAPI
		self.display()

	def display(self):
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

