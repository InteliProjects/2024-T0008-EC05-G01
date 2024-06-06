from classes.robot import RobotWrapper
from utils.text import printc, cstring
from enum import Enum
import typer
import yaspin


app = typer.Typer()

class Ferramenta(str, Enum):
	suction = "suction"
	gripper = "gripper"

@app.command(short_help="Liga uma ferramenta específica.")
def ligar(ferramenta: Ferramenta):
	"""
		Liga uma ferramenta específica

			- ferramenta: A ferramenta que deve ser ligada (suction ou gripper)

		Exemplo:

			$ python main.py ligar suction

			Isso ligará a ferramenta de sucção
	"""

	interagir_ferramenta(ferramenta.value, True)


@app.command(short_help="Desliga uma ferramenta específica.")
def desligar(ferramenta: Ferramenta):
	"""
		Desliga uma ferramenta específica

			- ferramenta: A ferramenta que deve ser desligada (suction ou gripper)

		Exemplo:

			$ python main.py desligar suction

			Isso desligará a ferramenta de sucção
	"""

	interagir_ferramenta(ferramenta.value, False)


def interagir_ferramenta(ferramenta: str, status: bool, robot = None):
	"""
		Liga ou desliga uma ferramenta específica, instanciando um robô caso não seja passado um como argumento
	"""

	if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))
	if not robot.initialized: robot.init()

	robot.tool(ferramenta, status)