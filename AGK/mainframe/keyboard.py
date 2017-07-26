import pygame
def pressed():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			return event.key

def down(key):
	return pygame.key.get_pressed()[key]

