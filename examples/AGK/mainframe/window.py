from attr import attrs, attrib, Factory
import pygame
@attrs
class window(object):
	title = attrib()
	width = attrib(default=Factory(lambda: 300))
	height = attrib(default=Factory(lambda: 200))

	def __attrs_post_init__(self):
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.title)

	def show(self):
		#show the window
		pygame.display.flip()

