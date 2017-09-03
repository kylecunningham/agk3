from attr import attrs, attrib, Factory
from ..speech import SAPI, auto
from ..mainframe import keyboard
from ..audio import sound
import pygame
@attrs
class menu_item(object):
	text = attrib()
	name = attrib()
	is_tts = attrib()
	is_enabled = attrib(default=Factory(bool))

@attrs
class menu(object):
	sapi = attrib(default=Factory(bool))
	run_sound = attrib(default=Factory(str))
	select_sound = attrib(default=Factory(str))
	move_sound = attrib(default=Factory(str))
	disabled_text = attrib(default=Factory(str))
	position = attrib(default=Factory(int))
	items = attrib(default=Factory(list), init=False)

	def add_item_tts(self,text,name,enabled=True):
		self.items.append(menu_item(text,name,True,enabled))

	def run(self,intro):
		if self.move_sound != "":
			self.move_sound_handle=sound.sound()
			self.move_sound_handle.load(self.move_sound)
		if self.select_sound != "":
			self.select_sound_handle=sound.sound()
			self.select_sound_handle.load(self.select_sound)
		self.speak(intro)
		self.position=-1

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key==pygame.K_UP:
						if self.position<=0:
							self.position=0
						else:
							self.position-=1
						self.speak(self.items[self.position].text)
						if self.items[self.position].is_enabled == False:
							self.speak("disabled")
						if self.move_sound != "":
							self.move_sound_handle.stop()
							self.move_sound_handle.play()
					if event.key==pygame.K_DOWN:
						if self.position<len(self.items)-1:
							self.position+=1
						self.speak(self.items[self.position].text)
						if self.items[self.position].is_enabled == False:
							self.speak("disabled")
						if self.move_sound != "":
							self.move_sound_handle.stop()
							self.move_sound_handle.play()


					if event.key==pygame.K_RETURN:
						if self.items[self.position].is_enabled == False:
							self.speak(self.disabled_text)
							break
						if self.select_sound != "":
							self.select_sound_handle.play()
						return self.items[self.position]

					if event.key==pygame.K_ESCAPE:
						return -1

#internal funcs
	def speak(self,text):
		if self.sapi==False:
			auto.speak(text)
		else:
			SAPI.speak(text)