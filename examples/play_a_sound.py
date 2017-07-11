#play a basic sound.
#first, we import the audio playing library.
from AGK.audio import sound
#next, we create a sound instance, called this time tick.
tick=sound.sound()
#then, we load the sound.
tick.load("snd/sound.ogg")
#then we play the sound wait. This means, the program executing pauses while the sound is playing.
tick.play_wait()