#-*-coding:Latin-1-*
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
	print("Batimentos cardíacos (bpm): "+ str(msg.payload))

broker_adress = "Endereço ipV4"
port = "1883"

client = mqtt.Client("Sub")
print("Cliente criado com sucesso")
client.connect(broker_adress,port)
print("Cliente Ligado com sucesso")
client.subscribe("Teste")
print("Cliente subscreveu o tópico (Teste) com sucesso")
client.on_message = on_message
client.loop_forever()

