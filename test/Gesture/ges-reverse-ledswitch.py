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
#LED,Gesture
import grove_gesture_sensor
from grovepi import *

#ほか
import time
import subprocess


#Json関連
import json
from collections import OrderedDict
#import pprint


routerFlag =False #セキュア回線をONにしている際にTrue(1)



def router():
#セキュア回線のONOFF関連のまとめ

    global routerFlag

                
    if routerFlag == True:
	#onにする
	sub=subprocess.call(['sudo','ip','l','set','wlan0','up'])
	if sub==1:
		print('トングル繋がってますか？')
	print("Turn on secure line")
	'''
	#hostapdで切り替える手法 セキュアと通常回線を両立しない場合に使用可能
	#subprocess.call(['sudo','sed','-i','s/Wi-Pi-OPEN.conf/hostapd.conf/g','/etc/default/hostapd'])
	#subprocess.call(['sudo','systemctl','restart','dhcpcd'])
	#subprocess.call(['sudo','systemctl','restart','hostapd'])
	'''
	led("send")
	
	
        print("router ON  routerFlag:"+ str(routerFlag))

	
    else:
	#off
	sub=subprocess.call(['sudo','ip','l','set','wlan1','down'])
	if sub==1:
		print('トングル繋がってますか？')
	print("Turn off secure line")
	'''
	#subprocess.call(['sudo','sed','-i','s/hostapd.conf/Wi-Pi-OPEN.conf/g','/etc/default/hostapd'])
	#subprocess.call(['sudo','systemctl','restart','dhcpcd'])
	#subprocess.call(['sudo','systemctl','restart','hostapd'])
	'''

	led("send")
	
	#routerFlag= True
	print("router OFF routerFlag:"+ str(routerFlag))
		



    
    
def led(job):
    global	routerFlag
    led = 7
    if job=="send":
	if (routerFlag==True):
		#Blink the LED
		digitalWrite(led,1)		# Send HIGH to switch on LED
		print ("router LED ON!")
		
	else:
		digitalWrite(led,0)		# Send LOW to switch on LED
		
    elif job=="recog":
	#Wi-Pi send
	
	    for num in range(5):
		#Blink the LED
		digitalWrite(led,1)     # Send HIGH to switch on LED
		print ("LED ON!")
		time.sleep(0.2)

		digitalWrite(led,0)     # Send LOW to switch off LED
		print ("LED OFF!")
		time.sleep(0.2)

def main():
    global routerFlag
    try:
	g=grove_gesture_sensor.gesture()
 	g.init() 
	print("Welcome to the Wi-Pi")    

    except IOError:
    #なぜかラズパイ起動後には必ず１回IOErrorが出るためリスタートしている 
	print("wake-up Error Resterting")
	main()
	pass
    
    try:
	while True:
	    gest=g.return_gesture()

	    #Match the gesture
	    if gest==g.FORWARD:
		print("FORWARD")
		
		led("recog")
		routerFlag =True
		router()
		time.sleep(1)

	    elif gest==g.DOWN:
		print("DOWN")
		
		led("recog")
		routerFlag =False
		router()
		time.sleep(1)   

		
	    else :
		time.sleep(.1)

    except IOError:#意図しない強制終了の際に、プログラムを再起動させる
	print("__________________/ntry/n________________")
	subprocess.Popen(['python','/home/pi/Desktop/Wi-Pi-System/test/Gesture/ges-reverse.py'])

	
	#現状では必要のないもの、再起動のログなどを残す場合には使えそう （その時はjson ではなくcsvかなんかで出したい）
	'''
	with open('/home/pi/Desktop/Wi-Pi-System/test/Data/Wi-Pi.json','w') as f:
	    df['routerFlag']=routerFlag
	    json.dump(df, f)
	'''
    except KeyboardInterrupt: 
	print("Ctrl +C ")
	digitalWrite(7,0)
	#↓プログラム強制終了時にセキュア回線をOFFにするため落とす
	#subprocess.call(['sudo','ip','l','set','wlan1','down'])
	print("Turn off secure line")
	print("See you")

if __name__ == '__main__':
    global routerflag
    with open('/home/pi/Desktop/Wi-Pi-System/test/Data/Wi-Pi.json','r') as f:
	df = json.load(f)
	routerFlag = df['routerFlag']
    main()
