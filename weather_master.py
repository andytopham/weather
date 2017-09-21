#!/usr/bin/python
# Main weather application. Currently just shows time.

import lcd, time, datetime
import rotary
import wunder
import keys

myLcd = lcd.Screen()
myLcd.clear()
myLcd.writerow(0,'Test')
myRotary = rotary.Rotary()
myWeather = wunder.Weather(keys.wunder,keys.locn)
old = time.time()
temp = myWeather.wunder(keys.wunder,keys.locn)

date = ''
count = 0
print "Entering permanant loop showing time"
while True:
	count = count + myRotary.read_count()
	new = time.time()
	if (new-old) > 60:		# restrict how frequently we ask wunder
		temp = myWeather.wunder(keys.wunder,keys.locn)
		old = new
	str1 = time.strftime(" %H:%M ")
	str1 = temp + str1 + "  " + str(count)
	myLcd.writerow(0, str1)
	str2 = time.strftime("%A %d %b")
	myLcd.writerow(1, str2)
	time.sleep(1)

