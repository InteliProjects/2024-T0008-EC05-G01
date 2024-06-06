import typer

from commands.interface import app as interface
from commands.mover import app as mover
from commands.atual import app as atual
from commands.ferramenta import app as ferramenta
from commands.home import app as home
from commands.montar_kit import app as montar_kit
from commands.redefinir_pos_kit import app as redefinir_pos_kit

app = typer.Typer()

app.registered_commands += interface.registered_commands
app.registered_commands += mover.registered_commands
app.registered_commands += atual.registered_commands
app.registered_commands += ferramenta.registered_commands
app.registered_commands += montar_kit.registered_commands
app.registered_commands += home.registered_commands
app.registered_commands += redefinir_pos_kit.registered_commands


if __name__ == "__main__":
	print("") #? Isso é só pra dar um espaço entre o prompt e o texto
	app()