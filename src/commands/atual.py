from classes.robot import RobotWrapper
from utils.text import printc, cstring
import typer
import yaspin


app = typer.Typer()

@app.command(short_help="Mostra a posição atual do robô.", name="atual")
def wrapper():
	"""
		Mostra a posição atual do robô

		Exemplo:

			$ python main.py atual

			Isso mostrará a posição atual do robô (X, Y, Z)
	"""

	atual()

def atual(robot = None):
	if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))
	if not robot.initialized: robot.init()

	curr_pos = robot.current()

	printc(f"[&6ROBOT&f] &bEu estou em &dX: {curr_pos['x']}&b, &dY: {curr_pos['y']}&b, &dZ: {curr_pos['z']}")

	return curr_pos