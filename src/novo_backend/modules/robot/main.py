from queue import Queue

from modules.robot.classes.KitAssembler import KitAssembler


def robot_daemon(queue: Queue):
	robot = KitAssembler()
	robot.robot.home()
	while True:
		kit = queue.get()
		print(f"Kit recebido: {kit}")
		robot.assemble(kit)
		# print(robot.get_pos())
