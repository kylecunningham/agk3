#in this example, we're going to print the letter "A" every 1 second
#import timer class.
from AGK.mainframe import timer
#create a timer
testtimer=timer.timer()
#loop forever
while 1:

#check if the timer has elapsed 1000 MS or 1 second
	if testtimer.elapsed()>=1000:
#then print A
		print ("a")
#restart the timer
		testtimer.restart()