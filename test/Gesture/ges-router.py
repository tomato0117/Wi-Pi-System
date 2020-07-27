# coding: UTF-8
#!/usr/bin/env python
#
# GrovePi Example for using the Grove - Gesture Sensor v1.0(http://www.seeedstudio.com/depot/Grove-Gesture-p-2463.html)
#       
# This example returns a value when a user does an action over the sensor
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import grove_gesture_sensor
import time
import subprocess
from grovepi import *

flag1 =False


time.sleep(1)


def router():
	
    global flag1
                
    if flag1 == 1:
	#onにする
	subprocess.call(['sudo','sed','-i','s/Wi-Pi-OPEN.conf/hostapd.conf/g','/etc/default/hostapd'])
	subprocess.call(['sudo','systemctl','restart','dhcpcd'])
	subprocess.call(['sudo','systemctl','restart','hostapd'])
	led()#処理例
	
        flag1=0
        print("router change :"+ str(flag1))

	
    else:
	#off
	subprocess.call(['sudo','sed','-i','s/hostapd.conf/Wi-Pi-OPEN.conf/g','/etc/default/hostapd'])
	subprocess.call(['sudo','systemctl','restart','dhcpcd'])
	subprocess.call(['sudo','systemctl','restart','hostapd'])
	led() #処理例
	flag1= 1 
	print("router change :"+ str(flag1))
		


def led():
	global	flag1
	led = 7
	if (flag1==1):
		#Blink the LED
		digitalWrite(led,1)		# Send HIGH to switch on LED
		print ("LED ON!")
		time.sleep(0.1)
		
	else:
		digitalWrite(led,0)		# Send LOW to switch on LED
		print ("LED OFF!")
		time.sleep(0.1)

def led_thread():#スレッドを使用点滅はWhileTrueを利用、点灯はbreakで抜けてくる、stopを引数に入れると完全に止まる
    led = 7
    while True:
	digitalWrite(led,1)     # Send HIGH to switch on LED
	print ("Thread-LED ON!")
	time.sleep(0.5)
                    
	digitalWrite(led,0)     # Send LOW to switch off LED
	print ("Thread-LED OFF!")
	time.sleep(0.5) 
	
    
	


def main():
    g=grove_gesture_sensor.gesture()
    g.init()
    while True:
        gest=g.return_gesture()
        #Match the gesture
        if gest==g.FORWARD:
            print("FORWARD")
 #           time.sleep(1)
            router()
            

        elif gest==g.RIGHT:
            print("RIGHT")
  #          time.sleep(1)
            router()
        elif gest==g.LEFT:
            
            print("LEFT")
   #         time.sleep(1)
            router()
            
        elif gest==g.UP:
            print("UP")
 #           time.sleep(1)
            router()
            
        elif gest==g.DOWN:
            print("DOWN")
 #           time.sleep(1)
            router()
            
"""
        elif gest==g.CLOCKWISE:
            print("CLOCKWISE")
    #        time.sleep(1)
            led()
        elif gest==g.ANTI_CLOCKWISE:
            print("ANTI_CLOCKWISE")
   #         time.sleep(1)
            led()
        elif gest==g.WAVE:
            print("WAVE")
   #         time.sleep(1)
            led()
        elif gest==0:
            print("-")
"""
    
if __name__ == '__main__':

    main()
