import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

while True:
	value = adc.read_adc(3, gain=GAIN)
	voltage = value * 4.096/65536 * 1000
	print("Voltage = %d" %voltage)
	time.sleep(1)

