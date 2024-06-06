from classes.robot import RobotWrapper
from utils.text import printc
import typer
import yaspin


app = typer.Typer()

@app.command(short_help="Move o robô para a sua posição \"home\".", name="home")
def wrapper():
	"""
		Move o robô para a sua posição "home"

		Exemplo:

			$ python main.py home

			Isso moverá o robô para a posição X: 100, mantendo as posições Y e Z
	"""

	home()


def home(robot = None):
	"""
		Move o robô para a sua posição "home"
	"""

	if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))
	if not robot.initialized: robot.init()

	curr_pos = robot.current()

	printc(f"[&6ROBOT&f] &bEu estou em &dX: {curr_pos['x']}&b, &dY: {curr_pos['y']}&b, &dZ: {curr_pos['z']}")

	printc(f"[&6ROBOT&f] &bIndo para &dHOME &b(&dX: {robot.constants['home']['x']}&b, &dY: {robot.constants['home']['y']}&b, &dZ: {robot.constants['home']['z']}&b)")

	robot.home()

	printc(f"[&6ROBOT&f] &aCheguei!")

	return robot.current()