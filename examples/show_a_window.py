#import
import pygame
from AGK.speech import auto
from AGK.mainframe import window, keyboard
#create a window.
w=window.window("test window")
w.show()
while 1:
#a test of key holder

	if keyboard.down(pygame.K_a):
		auto.speak("a")

	if keyboard.pressed()==pygame.K_ESCAPE:
		break