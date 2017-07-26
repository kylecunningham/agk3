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

@attrs
class EntryDialog(object):
	displaytext = attrib()
	SAPI = attrib(default=Factory(bool))

	def __attrs_post_init__(self):
		self.speak(self.displaytext + " To repeat, press F1.")
		self.do_entry()

	def do_entry(self):
		string = ""
		while 1:
			keyinput = pygame.key.get_pressed()  
			character = "NULL"

			# Get all "Events" that have occurred.
			pygame.event.pump()
			keyPress = keyboard.pressed()

			#If the user presses a key on the keyboard then get the character
			if keyPress >= 32 and keyPress <= 126:
				#If the user presses the shift key while pressing another character then capitalise it
				if keyinput[K_LSHIFT]: 
					keyPress -= 32

			character = chr(keyPress)

			if char == "NULL":
				continue
			elif char != "NULL":
				string = string + char
			for evt in pygame.event.get():
				if evt.type == pygame.KEYDOWN:
					if evt.key==pygame.K_F1:
						self.speak(self.displaytext)
					if evt.key == pygame.K_RETURN:
						return string
					if evt.key==pygame.K_ESCAPE:
						break

	def speak(self, text):
		if self.SAPI==True:
			SAPI.speak(text)
		else:
			auto.speak(text)
