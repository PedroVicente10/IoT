#-*-coding:Latin-1-*
import paho.mqtt.client as mqtt
import time
from influxdb import InfluxDBClient

def on_message(client, userdata, msg):
	print("Batimentos cardíacos (bpm): "+ str(msg.payload))
	iso = time.ctime()
	data = [
	{"measurement": measurement,
    "tags": {"location": location,},
    "time": iso,
    "fields": {"Batimentos Cardíacos (bpm)": str(msg.payload)}}
    ]
	client_influxdb.write_points(data)

broker_adress = "Endereço ipV4"
port1 = "1883"
port2 = "8086"
user = "admin"
password = "password"
dname = "Sensores"

client_influxdb = InfluxDBClient(broker_adress,port2,user,password,dname)
measurement = "Heart Beat"
location = "Finger"

client = mqtt.Client("Sub")
print("Cliente criado com sucesso")
client.connect(broker_adress,port1)
print("Cliente Ligado com sucesso")
client.subscribe("Teste")
print("Cliente subscreveu o tópico (Teste) com sucesso")
client.on_message = on_message
client.loop_forever()

