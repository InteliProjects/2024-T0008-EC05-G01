import threading

from modules.qrcode.main import perpetually_read

class QRCodeWrapper:
	def __init__(self, timeout: float = 0.25):
		self.thread = threading.Thread(target=perpetually_read)
		self.timeout = timeout

	def start(self):
		self.thread.start()

	def stop(self):
		self.thread.join(self.timeout)
