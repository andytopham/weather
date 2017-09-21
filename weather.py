#!/usr/bin/python
# Main weather application. Currently just shows time.

import lcd, time, datetime
import rotary

myLcd = lcd.Screen()
myLcd.clear()
myLcd.writerow(0,'Test')
myRotary = rotary.Rotary()
date = ''
count = 0
print "Entering permanant loop showing time"
while True:
	count = count + myRotary.read_count()
	now = datetime.datetime.now()
	str1 = time.strftime("     %H:%M")
	str1 = str1 + "  " + str(count)
	myLcd.writerow(0, str1)
	str2 = time.strftime("%A %d %b")
	myLcd.writerow(1, str2)
	time.sleep(1)

