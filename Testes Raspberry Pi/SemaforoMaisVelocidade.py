import RPi.GPIO as GPIO
from time import sleep

Time = 1
first = 36
second = 40
third = 38

def Velocity(self):
	print("Button pressed!")
	global Time
	Time = Time - 0.1


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(37, GPIO.RISING, callback= Velocity)


while True:
	GPIO.output(first,GPIO.HIGH)
	sleep(Time)
	GPIO.output(first,GPIO.LOW)
	GPIO.output(second,GPIO.HIGH)
	sleep(Time)
	GPIO.output(second,GPIO.LOW)
	GPIO.output(third,GPIO.HIGH)
	sleep(Time)
	GPIO.output(third,GPIO.LOW)
