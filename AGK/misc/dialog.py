from attr import attrs, attrib, Factory
from ..speech import auto, SAPI
from ..mainframe import keyboard
from ..audio import sound
import pygame
from pygame.locals import *

@attrs
class dialog(object):
	text = attrib()
	type=attrib(default=Factory(int))
	popup_sound = attrib(default=Factory(str))
	SAPI = attrib(default=Factory(bool))

	def __attrs_post_init__(self):
		if self.type:
			self.display(self.type)
		else:
			self.display()

	def display(self,type=1):
		if self.popup_sound != "":
			handle = sound.sound()
			handle.load(self.popup_sound)
			handle.play()
		if type==1:
			speak(self.text + " To repeat, press R. To dismiss, press enter.",self.SAPI)
		elif type==2:
			speak(self.text)
		while 1:
			for evt in pygame.event.get():
				if evt.type == pygame.KEYDOWN:
					if type==1:
						if evt.key==pygame.K_r:
							speak(self.text,self.SAPI)
					elif type==2:
						if evt.key==pygame.K_LEFT or evt.key==pygame.K_RIGHT or evt.key==pygame.K_DOWN or evt.key==pygame.K_UP:
							speak(self.text)
						elif evt.key==pygame.K_RETURN or evt.key==pygame.K_SPACE:
							return 1
					if evt.key == pygame.K_RETURN:
						return 1

@attrs
class EntryDialog(object):
	displaytext = attrib()
	type_sound = attrib(default=Factory(str))
	SAPI = attrib(default=Factory(bool))
	string = attrib(default=Factory(str))
	speak_chars=attrib(default=Factory(bool))

	def __attrs_post_init__(self):
		if self.type_sound != "":
			self.type_handle = sound.sound()
			self.type_handle.load(self.type_sound)
		speak(self.displaytext + " To repeat, press F1, to toggle speaking of characters, press f2.",self.SAPI)
		self.CatchInput()


	def CatchInput(self):
		while True:
			for evt in pygame.event.get():
				if evt.type == KEYDOWN:
					if evt.unicode.isalpha():
						if self.type_sound != "":
							self.type_handle.play()
						if self.speak_chars:
							speak(evt.unicode,self.SAPI)
						self.string += evt.unicode
					elif evt.key == K_SPACE:
						self.string += " "
						if self.speak_chars:
							speak("space",self.SAPI)
					elif evt.key == K_BACKSPACE:
						if len(self.string)>0:
							speak(self.string[-1]+" deleted",self.SAPI)
						self.string = self.string[:-1]
					elif evt.key == K_UP or evt.key == K_DOWN:
						speak(self.string,self.SAPI)
					elif evt.key == K_F1:
						speak(self.displaytext,self.SAPI)
					elif evt.key==K_F2:
						if self.speak_chars:
							self.speak_chars=False
							speak("speak typed characters disabled",self.SAPI)
						elif not self.speak_chars:
							self.speak_chars=True
							speak("speak typed characters enabled",self.SAPI)
					elif evt.key == K_RETURN:
						return self.string

def speak(text, SAPI=False):
	if SAPI:
		SAPI.speak(text)
	else:
		auto.speak(text)