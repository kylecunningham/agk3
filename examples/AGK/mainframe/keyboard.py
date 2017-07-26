import pygame
def pressed():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			return event.key

def down(key):
	return pygame.key.get_pressed()[key]

def getCharacter():
	keyinput = pygame.key.get_pressed()  
	character = "NULL"

	# Get all "Events" that have occurred.
	pygame.event.pump()
	keyPress = pressed()

	#If the user presses a key on the keyboard then get the character
	if keyPress >= 32 and keyPress <= 126:
	#If the user presses the shift key while pressing another character then capitalise it
		if keyinput[K_LSHIFT]: 
			keyPress -= 32

		character = chr(keyPress)

	return character 