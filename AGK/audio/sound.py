from attr import attrs, attrib, Factory
import sound_lib
from sound_lib import output
from sound_lib import stream
o=output.Output()
@attrs
class sound():
	handle=attrib(default=Factory(int))
	def load(self,filename=""):
		self.handle =stream.FileStream(file=filename)
	def play(self):
		self.handle.looping=False
		self.handle.play()
	def play_wait(self):
		self.handle.looping=False
		self.handle.play_blocking()
	def play_looped(self):
		self.handle.looping=True
		self.handle.play()
	def stop(self):
		if not self.handle==0:
			self.handle.stop()
			self.handle.set_position(0)
	def set_volume(self, new_volume):
		self.handle.set_volume(new_volume)
