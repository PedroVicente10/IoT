import RPi.GPIO as GPIO
from time import sleep

Time = 1
first = 36
second = 40
third = 38

def MaisVelocidade(self):
	print("Button pressed! Mais Velocidade!")
	global Time
	if Time - 0.1 <= 0:
		Time = 0.05
	else:
		Time = Time - 0.1

def MenosVelocidade(self):
	print("Button pressed! Menos Velocidade!")
	global Time
	Time = Time + 0.1


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(37, GPIO.RISING, callback= MaisVelocidade)
GPIO.add_event_detect(35, GPIO.RISING, callback= MenosVelocidade)


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
