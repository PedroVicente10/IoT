import time
import Adafruit_ADS1x15
import zmq

host = "192.168.1.124"
port = "5001"

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind("tcp://{}:{}".format(host,port))

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

while True:
	value = adc.read_adc(3, gain=GAIN)
	voltage = value * 4.096/65536 * 1000
	msg = "Value =  %d" %voltage
	print("A transmitir: %d" %voltage)
	socket.send_string(msg)
	time.sleep(1)

socket.close()
context.term()
