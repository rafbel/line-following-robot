#!/usr/bin/python

import time
import RPi.GPIO as GPIO

leftSensor = 22
rightSensor = 18
middleSensor = 11

GPIO.setmode(GPIO.BCM)

GPIO.setup(leftSensor,GPIO.IN)
GPIO.setup(rightSensor,GPIO.IN)
GPIO.setup(middleSensor,GPIO.IN)

while (True):
	
	left   = GPIO.input(leftSensor)
	middle = GPIO.input(middleSensor)
	right  = GPIO.input(rightSensor)

	print 'L:' + str(left) + ' M:' + str(middle) + ' R:' + str(right)
 
 	time.sleep(0.1)
