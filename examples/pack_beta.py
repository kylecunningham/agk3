#This is still work in progress
import time
from AGK import audio
#initialize the class
pack=audio.packer.packer()
#add a file to our pack
pack.add_file("sounds.dat","snd/l.ogg")
#encrypt our pack and store the key in the variable.
deckey=pack.encrypt_file("abc","sounds.dat")
#load up libaudioverse
w=audio.sound3d.audio_world()
#set up so the sound loader sees our pack
sl=audio.sound3d.SoundLoader(world=w.world,server=w.server,pack="sounds.dat.enc",key=deckey)
#now, let's try to load a sound.
s=sl.load_sound("snd/l.ogg")
s.play()
time.sleep(1)