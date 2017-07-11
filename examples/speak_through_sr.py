#This example will show you how to speak a simple string through your currently selected screen reader
#import time, in order to delay the code while the screen reader speaks.
import time
#import the auto speaker from the speech module
from AGK.speech import auto
#speak the text.
auto.speak("This is a test.")
#Sleep so the speech has time to finish.
time.sleep(1)