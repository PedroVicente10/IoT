import RPi.GPIO as GPIO
from time import sleep

DC = 25


def MaisLuz(self):
	print("Mais Luz")
	global DC
	DC = DC + 1
	pwm.ChangeDutyCycle(DC)

def MenosLuz(self):
	print("Menos Luz")
	global DC
	DC = DC - 1
	pwm.ChangeDutyCycle(DC)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(37,GPIO.RISING,callback=MenosLuz)
GPIO.add_event_detect(35,GPIO.RISING,callback=MaisLuz)

GPIO.setup(40,GPIO.OUT)
pwm = GPIO.PWM(40,100)
pwm.start(DC)

while True:
	global DC
	print("DC = %d" % (DC))
	sleep(1)
