#the sound3d is still broken slightly, but this code will run.
#import things
import time
from AGK.audio import sound3d as s3d
#create the world
world=s3d.audio_world(reverbtime=0.2)
#create a sound loader.
sl=s3d.SoundLoader(world.server,world.world)
#load two sounds, left and right.
click1=sl.load_sound("snd/l.ogg")
click2=sl.load_sound("snd/r.ogg")
#position them.
click1.source.position=-10,0,1
click2.source.position=10,0,0
#the values are x, y, and z.
#play click1.
click1.play()
#sleep
time.sleep(1)
#play click2
click2.play()
#sleep
time.sleep(1)
#shutdown the world.
world.shutdown()