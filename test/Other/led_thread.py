# coding: UTF-8

import time
from grovepi import *
import grove_gesture_sensor

#~ def main():
led = 7


while True:
		#Blink the LED
		digitalWrite(led,1)		# Send HIGH to switch on LED
		print ("th-LED ON!")
		time.sleep(0.5)
		
		digitalWrite(led,0)		# Send LOW to switch on LED
		print ("th-LED OFF!")
		time.sleep(0.5)
			
	    
#~ if __name__ == '__main__':
    #~ main()

    
