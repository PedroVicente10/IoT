import RPi.GPIO as GPIO
from time import sleep

Raising = 1
DC = 0
DCI = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)

Laser = GPIO.PWM(35,1000)
Laser.start(DC)

Button = GPIO.input(37)

while True:
	Button = GPIO.input(37)
	if Button == False:
		DC = 0
	else:
		if Raising == 1:
			DC = DCI
			DC = DC + 1
			DCI = DC
			if DC >= 100:
				Raising = 0
		else:
			DC = DCI
			DC = DC - 1
			DCI = DC
			if DC <= 0:
				Raising = 1
	sleep(0.2)
	print("Brightness = %d %%" %(DC))
	Laser.ChangeDutyCycle(DC)
