import pygame
class window(object):
	def __init__(self,title):
		self.title=title

		(self.width, self.height) = (300, 200)
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(title)

	def show(self):
#show the window

		pygame.display.flip()

