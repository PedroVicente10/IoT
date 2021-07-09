import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)

while True:
	GPIO.output(36,GPIO.HIGH)
	sleep(1)
	GPIO.output(36,GPIO.LOW)
	GPIO.output(40,GPIO.HIGH)
	sleep(1)
	GPIO.output(40,GPIO.LOW)
	GPIO.output(38,GPIO.HIGH)
	sleep(1)
	GPIO.output(38,GPIO.LOW)
