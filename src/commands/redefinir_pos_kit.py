from classes.robot import RobotWrapper
from utils.text import printc, cstring
import inquirer
import yaspin
import typer
import json

app = typer.Typer()

@app.command(short_help="Redefine a posição de um medicamento", name="montar-kit")
def redefinir_pos_kit(robot):
    """
        Redefine a posição de um medicamento.

        Exemplo:

            $ python main.py redefinir_pos_kit

            $ Escolha o medicamento que você quer redefinir a posição

            $ Medicamento 1

            $ Medicamento 2

            $ Medicamento 3

        Ao escolher um medicamento, você deverá levar o robô até a posição desejada e apertar Enter.
    """
    if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))
    if not robot.initialized: robot.init()

    with open("./constants.json", "r") as arquivo:
        dados = json.load(arquivo)

    kits = [medicamento['nome'] for medicamento in dados.get("medicamentos", [])]

    respostas = inquirer.prompt([
        inquirer.List("kit", message="Escolha o medicamento para redefinir sua posição", choices=kits)
    ])

    printc(f"[&6ROBOT&f] &bLeve o robô até a posição desejada para o &5{respostas['kit']}")
    continuar = inquirer.prompt([inquirer.Confirm("new_pos", message="Deseja continuar e redefinir a posição do medicamento?")])
    if continuar == False:
        return
    else:
        robot.update_pos()
        medicamento = next((medicamento for medicamento in dados.get("medicamentos", []) if medicamento['nome'] == respostas['kit']), None)
        medicamento['posicao'] = {
            "x": robot.current()['x'],
            "y": robot.current()['y'],
            "z": robot.current()['z'],
            "r": 0.0
        }

        with open("./constants.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        robot.home()
        printc(f"[&6ROBOT&f] &aPosição do medicamento &5{respostas['kit']}&a redefinida com sucesso!")
        return
