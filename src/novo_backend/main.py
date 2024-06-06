import signal

from queue import Queue

from classes.ApiWrapper import ApiWrapper
from classes.RobotWrapper import RobotWrapper
from classes.QRCodeWrapper import QRCodeWrapper
from classes.SensorWrapper import SensorWrapper

wrappers = []


def main():
	queue = Queue()

	wrappers.append(ApiWrapper(queue))
	wrappers.append(RobotWrapper(queue))
	wrappers.append(SensorWrapper())
	wrappers.append(QRCodeWrapper())

	list(map(lambda wrapper: wrapper.start(), wrappers))

def exit_gracefully(signal, frame):
	list(map(lambda wrapper: wrapper.stop(), wrappers))
	exit()

# REMAP SIGINT AND SIGTERM TO exit_gracefully
signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)

if __name__ == "__main__":
	main()