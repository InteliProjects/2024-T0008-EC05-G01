import threading
from queue import Queue

from modules.api.main import start_api


class ApiWrapper:
	def __init__(self, queue: Queue, timeout: float = 0.25):
		self.thread = threading.Thread(target=start_api, args=(queue,))
		self.timeout = timeout

	def start(self):
		self.thread.start()

	def stop(self):
		self.thread.join(self.timeout)
