# coding: UTF-8
import json
from collections import OrderedDict
import pprint


with open('/home/pi/Desktop/Wi-Pi-System/test/Data/test.json','r') as f:
	df = json.load(f)
	pprint.pprint(df, width=40)
	print(df['add']['X'])
	df['add']['X']=(df['add']['X'])+100
	
	text = df['key']
	print(text)
	#pprint.pprint(df['add']['X'])
	pprint.pprint(df['add']['X'])
	
	if (df['add']['X'] == 900):
		print('900 yeahhhhhhh')
	if (df['name'] == "Bob"):
		print("Your Bob!!!")

	if (df['key'] == "MAN"):
		print("man!!!!")

with open('/home/pi/Desktop/Wi-Pi-System/test/Data/test.json','w') as f:
	json.dump(df, f)
	


	
