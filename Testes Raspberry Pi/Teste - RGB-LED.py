import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(35,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
Blue = GPIO.PWM(38,1000)
BDC = 100
Blue.start(BDC)
Green = GPIO.PWM(35,1000)
GDC = 0
Green.start(GDC)
Red = GPIO.PWM(40,1000)
RDC = 0
Red.start(RDC)

while True:
	while GDC != 100:
		GDC = GDC + 1
		Green.ChangeDutyCycle(GDC)
		sleep(0.05)
		BDC = BDC - 1
		Blue.ChangeDutyCycle(BDC)
		sleep(0.05)
	while RDC != 100:
		RDC = RDC + 1
		Red.ChangeDutyCycle(RDC)
		sleep(0.05)
		GDC = GDC - 1
		Green.ChangeDutyCycle(GDC)
		sleep(0.05)
	while BDC != 100:
		BDC = BDC + 1
		Blue.ChangeDutyCycle(BDC)
		sleep(0.05)
		RDC = RDC - 1
		Red.ChangeDutyCycle(RDC)
		sleep(0.05)
