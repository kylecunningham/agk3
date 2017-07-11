#play a basic sound, positioned on your left.
#first, we import the audio playing library.
import time
from AGK.audio import sound
#next, we import the positioning functions.
from AGK.audio import sound_positioning as sp
#let's create variables for our positions.
my_x=0
sound_x=-5
#next, we create a sound instance, called this time tick.
tick=sound.sound()
#then, we load the sound.
tick.load("snd/sound.ogg")
#then we play the sound looping.
#then, we position the sound. We actually need to use the handle for now, but that will be changed.
sp.position_sound_1d(tick.handle,my_x,sound_x,1,1)
tick.play_looped()
#then, we sleep so you can hear the sound.
time.sleep(1)