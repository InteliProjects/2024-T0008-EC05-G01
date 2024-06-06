from modules.sensor.utils.ports import serial_ports
from pubsub import pub
from serial import Serial
import json
import time

# Setup serial connection (adjust the port accordingly)

def sensor_daemon():
	ports = serial_ports()
	if len(ports) > 1: raise Exception("Mais de um raspberry pi pico conectado. Como pode????")
	if len(ports) == 0: raise Exception("Nenhum raspberry pi pico conectado")
	ser = Serial(ports[0])
	toggled = False

	print("Serial connection established")
	while True:
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			try:
				data = int(json.loads(line)['data'])
				# print(data)
				# pub.sendMessage("sensor_data", data=data)
				if data > 1000 and not toggled:
					toggled = True
					pub.sendMessage("sensor_data", data=toggled)
				elif data < 1000 and toggled:
					toggled = False
					pub.sendMessage("sensor_data", data=toggled)

			except json.JSONDecodeError:
				print(f"Invalid JSON: {line}")
		time.sleep(0.01)