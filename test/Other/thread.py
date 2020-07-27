# coding: UTF-8

import logging
import threading
import time
from grovepi import *

#logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
try:
	def worker1():
		led =7
		while True:
			digitalWrite(led,1)     # Send HIGH to switch on LED
			print ("Thread-LED ON!")
			time.sleep(0.5)
							
			digitalWrite(led,0)     # Send LOW to switch off LED
			print ("Thread-LED OFF!")
			time.sleep(0.5) 


	def worker2():
		num =0
		while True:
			print(num)
			num+=1
			time.sleep(1)
		
	if __name__ == '__main__':
		t1 = threading.Thread(target=worker1)
		# スレッドのデーモン化
		t1.setDaemon(True)
		t2 = threading.Thread(target=worker2)
		t1.start()
		t2.start()
		print('started')


except KeyboardInterrupt:   # Turn LED off before stopping
	print("stop")
	digitalWrite(led,0)
