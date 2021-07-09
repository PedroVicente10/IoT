#-*-coding:Latin-1-*
import time
import Adafruit_ADS1x15
import paho.mqtt.client as mqtt

broker_adress="Enderço ipV4"
client = mqtt.Client("Pub")
print("Cliente criado com sucesso")
client.connect(broker_adress)
print("cliente conectado com sucesso")

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

while True:
	value = adc.read_adc(3, gain=GAIN)
	voltage = value * 4.096/65536 * 1000
	client.publish("Teste",voltage)
	print("Informação enviada = %f" %voltage)
	time.sleep(1)
