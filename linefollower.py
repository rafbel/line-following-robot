#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import RPi.GPIO as GPIO


# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

leftSensor = 22
rightSensor = 18
middleSensor = 11

lapCounter = 0

rightservoMin = 400
rightservoMax = 420

leftservoMin = 380  # Min pulse length out of 4096
leftservoMax = 360  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
GPIO.setmode(GPIO.BCM)

GPIO.setup(leftSensor,GPIO.IN)
GPIO.setup(rightSensor,GPIO.IN)
GPIO.setup(middleSensor,GPIO.IN)
while (True):
	
	left=GPIO.input(leftSensor)
	middle=GPIO.input(middleSensor)
	right=GPIO.input(rightSensor)

	print 'L:' + str(left) + ' M:' + str(middle) + ' R:' + str(right)
 
	if middle and left and right:
		lapCounter += 1
	
	elif middle and left:
		
		pwm.setPWM(1, 0, leftservoMin)
  		pwm.setPWM(0, 0, rightservoMax)
	
	elif left:
		
		pwm.setPWM(1,0,0)
		pwm.setPWM(0,0,rightservoMin)

	elif right and middle:
		
		pwm.setPWM(1,0,leftservoMax)
		pwm.setPWM(0,0,rightservoMin)

	elif right:
		
		pwm.setPWM(1,0,leftservoMin)
		pwm.setPWM(0,0,0)

	else:
		
		pwm.setPWM(1,0,leftservoMin)
		pwm.setPWM(0,0,rightservoMin)

	
 	time.sleep(0.1)
