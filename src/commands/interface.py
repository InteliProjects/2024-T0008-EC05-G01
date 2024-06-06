from utils.text import cstring, printc
from classes.robot import RobotWrapper
import inquirer
import yaspin
import typer

from commands.home import home
from commands.mover import move
from commands.ferramenta import interagir_ferramenta
from commands.atual import atual
from commands.montar_kit import montar_kit
from commands.redefinir_pos_kit import redefinir_pos_kit

app = typer.Typer()

@app.command(short_help="Abre a interface do robô, com comandos para movimentação e controle do atuador", name="interface")
def wrapper():
	"""
		Abre uma interface de comunicação com o robô constante com o robô.

		Exemplo:

			$ python main.py interface

			Isso abrirá a interface de comunicação com o robô
	"""

	interface()

def interface(robot = None):
	choices=["HOME", "ATUADOR_ON", "MOVIMENTAR", "POS_ATUAL", "MONTAR_KIT", "REDEFINIR_POS_KIT", "SAIR"]
	if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))

	while True:
		try:
			respostas_main = inquirer.prompt([
				inquirer.List("interface", message=cstring("&bQual comando você quer executar?"), choices=choices),
			], raise_keyboard_interrupt=True)

			processar(respostas_main, robot, choices)
		except KeyboardInterrupt:
			printc(cstring("&cSaindo da interface..."))
			break


def processar(respostas_main, robot, choices):
	match respostas_main["interface"]:
		case "HOME":
			home(robot)
			choices.remove("HOME")

		case "ATUADOR_ON":
			interagir_ferramenta("suction", True, robot)
			choices.remove("ATUADOR_ON")
			choices.insert(choices.index("MOVIMENTAR"), "ATUADOR_OFF")

		case "ATUADOR_OFF":
			interagir_ferramenta("suction", False, robot)
			choices.remove("ATUADOR_OFF")
			choices.insert(choices.index("MOVIMENTAR"), "ATUADOR_ON")

		case "MOVIMENTAR":
			move(robot)
			if "HOME" not in choices: choices.insert(0, "HOME")

		case "POS_ATUAL":
			atual(robot)

		case "MONTAR_KIT":
			montar_kit(robot)

		case "REDEFINIR_POS_KIT":
			redefinir_pos_kit(robot)

		case "SAIR":
			raise KeyboardInterrupt

		case _:
			printc(cstring("&cComando inválido!"))