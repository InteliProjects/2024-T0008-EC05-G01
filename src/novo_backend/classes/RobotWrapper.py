import threading

from queue import Queue

from modules.robot.main import robot_daemon

class RobotWrapper:
	def __init__(self, queue: Queue, timeout: float = 0.25):
		self.thread = threading.Thread(target=robot_daemon, args=(queue,))
		self.timeout = timeout

	def start(self):
		self.thread.start()

	def stop(self):
		self.thread.join(self.timeout)
