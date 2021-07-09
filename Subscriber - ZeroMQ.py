from time import sleep
import zmq

host = "192.168.1.124"
port = "5001"

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://{}:{}".format(host,port))
socket.subscribe("")

while True:
	msg = socket.recv_string()
	print("A receber: %s" %msg)

socket.close()
context.term()
