from classes.robot import RobotWrapper
from enum import Enum
from typing_extensions import Annotated
from utils.text import printc, cstring
import inquirer
import yaspin
import typer


app = typer.Typer()

class Pos(str, Enum):
	x = "x"
	y = "y"
	z = "z"

@app.command(short_help="Move o robô para uma posição específica.")
def mover(posição: Pos, valor: Annotated[float, typer.Option(prompt=True)]):
	"""
		Move o robô para uma posição específica

			- posicao: A posição que o robô deve se mover (x, y ou z)

			- valor: O valor que a posição deve ter

		Exemplo:

			$ python main.py mover x

			$ Valor: 100

			Isso adiciona 100 à posição X do robô (mantendo as posições Y e Z)
	"""

	match posição.value:
		case "x":
			move(x=valor, add=True)
		case "y":
			move(y=valor, add=True)
		case "z":
			move(z=valor, add=True)


@app.command(short_help="Move o robô para uma posição específica", name='mover-para')
def mover_para():
	move()


def move(robot = None, x: float = 0, y: float = 0, z: float = 0, add=False):
	if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))
	if not robot.initialized: robot.init()

	curr_pos = robot.current()

	if not x and not y and not z:
		respostas = inquirer.prompt([
			inquirer.Text("x", message=cstring("&bDigite a coordenada &dX")),
			inquirer.Text("y", message=cstring("&bDigite a coordenada &dY")),
			inquirer.Text("z", message=cstring("&bDigite a coordenada &dZ"))
		])

		x = respostas['x']
		y = respostas['y']
		z = respostas['z']


	if add:
		x = float(x) + curr_pos['x']
		y = float(y) + curr_pos['y']
		z = float(z) + curr_pos['z']
	else:
		if not x: x = curr_pos['x']
		if not y: y = curr_pos['y']
		if not z: z = curr_pos['z']


	printc(f"[&6ROBOT&f] &bEu estou em X: &d{curr_pos['x']}&b, Y: &d{curr_pos['y']}&b, Z: &d{curr_pos['z']}")

	printc(f"[&6ROBOT&f] &bIndo para X: &d{x}&b, Y: &d{y}&b, Z: &d{z}")

	robot.move(float(x), float(y), float(z))

	printc(f"[&6ROBOT&f] &aCheguei!")

	return { "x": x, "y": y, "z": z }