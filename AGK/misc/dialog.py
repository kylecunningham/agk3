from attr import attrs, attrib, Factory
from ..speech import auto, SAPI
from ..mainframe import keyboard
from ..audio import sound
import pygame
from pygame.locals import *

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

@attrs
class EntryDialog(object):
	displaytext = attrib()
	type_sound = attrib(default=Factory(str))
	SAPI = attrib(default=Factory(bool))
	string = attrib(default=Factory(str))

	def __attrs_post_init__(self):
		if self.type_sound != "":
			self.type_handle = sound.sound()
			self.type_handle.load(self.type_sound)
		self.speak(self.displaytext + " To repeat, press F1.")
		self.do_entry()

	def do_entry(self):
		self.speak(self.displaytext + " To repeat, press F1.")
		self.CatchInput()

	def speak(self, text):
		if self.SAPI==True:
			SAPI.speak(text)
		else:
			auto.speak(text)

	def CatchInput(self):
		while True:
			for evt in pygame.event.get():
				if evt.type == KEYDOWN:
					if evt.unicode.isalpha():
						if self.type_sound != "":
							self.type_handle.play()
						self.speak(evt.unicode)
						self.string += evt.unicode
					elif evt.key == K_SPACE:
						self.string += " "
					elif evt.key == K_BACKSPACE:
						self.speak("character deleted")
						self.string = self.string[:-1]
					elif evt.key == K_UP or evt.key == K_DOWN:
						self.speak(self.string)
					elif evt.key == K_F1:
						self.speak(self.displaytext)
					elif evt.key == K_RETURN:
						return self.string

