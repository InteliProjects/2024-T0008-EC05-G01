import threading

from modules.sensor.main import sensor_daemon

class SensorWrapper:
	def __init__(self, timeout: float = 0.25):
		self.thread = threading.Thread(target=sensor_daemon)
		self.timeout = timeout

	def start(self):
		self.thread.start()

	def stop(self):
		self.thread.join(self.timeout)
