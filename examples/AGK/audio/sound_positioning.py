import math

"""
#Sound Positioning Functions
#
#This file contains a collection of functions that will make dealing with sound positioning in an environment considerably easier. The functions have support for 1 dimentional environments such as those seen in side scrolling games, as well as 2 dimentional ones where the user moves along both an x and a y axis.
"""

def position_sound_1d(handle,  listener_x,  source_x,  pan_step,  volume_step) :
 position_sound_custom_1d(handle, listener_x, source_x, pan_step, volume_step, 0.0, 0.0)
 

def position_sound_custom_1d(handle,  listener_x,  source_x,  pan_step,  volume_step,  start_pan,  start_volume):
 delta=0
 final_pan=start_pan
 final_volume=start_volume
 
 # First, we calculate the delta between the listener and the source.
 if(source_x<listener_x):
  delta=listener_x-source_x
  final_pan-=(delta*pan_step)
  final_volume-=(delta*volume_step)
 
 if(source_x>listener_x):
  delta=source_x-listener_x
  final_pan+=(delta*pan_step)
  final_volume-=(delta*volume_step)
 
 # Now we set the properties on the sound, provided that they are not already correct.
 fp=float(final_pan/10.0)
 fv=float(final_volume/10.0)
 if fp<=-1:
  fp=-1
 if fp>=1:
  fp=1
 if fv<=-1:
  fv=-1
 if fv>=1.0:
  fv=1
 try:
  handle.pan=fp
 except:
  pass
 try:
  handle.volume=1+fv
 except:
  pass

def position_sound_2d(handle,  listener_x,  listener_y,  source_x,  source_y,  pan_step,  volume_step,  behind_pitch_decrease,  behind_volume_decrease=0):
 position_sound_custom_2d(handle, listener_x, listener_y, source_x, source_y, pan_step, volume_step, behind_pitch_decrease, behind_volume_decrease, 0.0, 0.0, 100.0)


def position_sound_custom_2d(handle,  listener_x,  listener_y,  source_x,  source_y,  pan_step,  volume_step,  behind_pitch_decrease,  behind_volume_decrease,  start_pan,  start_volume,  start_pitch):
 delta_x=0
 delta_y=0
 final_pan=start_pan
 final_volume=start_volume
 final_pitch=start_pitch
 
 # First, we calculate the delta between the listener and the source.
 if(source_x<listener_x):
  delta_x=listener_x-source_x
  final_pan-=(delta_x*pan_step)
  final_volume-=(delta_x*volume_step)
 
 if(source_x>listener_x):
  
  delta_x=source_x-listener_x
  final_pan+=(delta_x*pan_step)
  final_volume-=(delta_x*volume_step)
 
 if(source_y<listener_y):
  final_pitch-=abs(behind_pitch_decrease)
  final_volume-=abs(behind_volume_decrease)
  delta_y=listener_y-source_y
  final_volume-=(delta_y*volume_step)
 
 if(source_y>listener_y):
  delta_y=source_y-listener_y
  final_volume-=(delta_y*volume_step)
 
 
 # Now we set the properties on the sound, provided that they are not already correct.
 fp=float(final_pan/10.0)
 fv=float(final_volume/10.0)
 if fp<=-1:
  fp=-1
 if fp>=1:
  fp=1
 if fv<=-1:
  fv=-1
 if fv>=1:
  fv=1
 try:
  handle.pan=fp
 except:
  pass
 try:
  handle.volume=1+fv
 except:
  pass

def position_sound_3d(handle,  listener_x,  listener_y,  listener_z,  source_x,  source_y,  source_z,  pan_step,  volume_step,  behind_pitch_decrease,  behind_volume_decrease=0):
 position_sound_custom_2d(handle, listener_x, listener_y, listener_z, source_x, source_y, source_z, pan_step, volume_step, behind_pitch_decrease, behind_volume_decrease, 0.0, 0.0, 100.0)

def position_sound_custom_3d(handle,  listener_x,  listener_y,  listener_z,  source_x,  source_y,  source_z,  pan_step,  volume_step,  behind_pitch_decrease,  behind_volume_decrease,  pitch_step,  pitch_range,  start_pan,  start_volume,  start_pitch):
 delta_x=0
 delta_y=0
 delta_z=0
 final_pan=start_pan
 final_volume=start_volume
 final_pitch=start_pitch
 
 # First, we calculate the delta between the listener and the source.
 if(source_x<listener_x):
  delta_x=listener_x-source_x
  final_pan-=(delta_x*pan_step)
  final_volume-=(delta_x*volume_step)
 
 if(source_x>listener_x):
  delta_x=source_x-listener_x
  final_pan+=(delta_x*pan_step)
  final_volume-=(delta_x*volume_step)
 
 if(source_y<listener_y):
  final_pitch-=abs(behind_pitch_decrease)
  final_volume-=abs(behind_volume_decrease)
  delta_y=listener_y-source_y
  final_volume-=(delta_y*volume_step)
 
 if(source_y>listener_y):
  delta_y=source_y-listener_y
  final_volume-=(delta_y*volume_step)
 
 delta_z=abs(source_z-listener_z)
 final_volume-=delta_z*volume_step*0.5 # Z should have the least effect on volume.
 if(source_z<listener_z) :
  delta_pitch=pitch_step*(listener_z-source_z)
  if(delta_pitch>pitch_range):
   delta_pitch=pitch_range
  final_pitch-=delta_pitch
 
 if(source_z>listener_z) :
  delta_pitch=(source_z-listener_z)*pitch_step
  if(delta_pitch>pitch_range):
   delta_pitch=pitch_range
  final_pitch+=delta_pitch
 
 
 # Now we set the properties on the sound, provided that they are not already correct.
 fp=float(final_pan/10.0)
 fv=float(final_volume/10.0)
 if fp<=-1:
  fp=-1
 if fp>=1:
  fp=1
 if fv<=-1:
  fv=-1
 if fv>=1:
  fv=1
 try:
  handle.pan=fp
 except:
  pass
 try:
  handle.volume=1+fv
 except:
  pass