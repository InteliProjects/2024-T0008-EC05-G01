from tinydb import Query
import time
from threading import Thread

from pubsub import pub

from modules.robot.classes.robot import RobotWrapper
from modules.robot.classes.Kit import Kit
from modules.robot.classes.Pos import Pos
from database.wrapper import DB


class KitAssembler:
	robot = RobotWrapper(auto_init=True)

	def __init__(self):
		self.should_stop = False
		self.assembling = False
		pub.subscribe(self.stop_during, "sensor_data")
		pass


	def get_pos(self):
		"""
			Retorna a posição atual do robô
		"""
		return self.robot.current()

	def assemble(self, kit: dict):
		"""
			Recebe um kit e monta ele
		"""
		try: kit_obj = Kit(kit)
		except Exception as e: raise Exception(f"Erro ao criar o kit: {e}")

		with DB('database/archives/kits.json') as kits_db:
			if len(kits_db.search(Query().nome == kit_obj.nome)) <= 0:
				raise Exception("Kit não cadastrado")

		for medicamento in kit_obj.medicamentos:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamento_estoque = medicamentos_db.search(Query().nome == medicamento.nome)

			if len(medicamento_estoque) <= 0:
				raise Exception(f"Medicamento {medicamento.nome} não cadastrado")

			medicamento_estoque = medicamento_estoque[0]
			get_pos = Pos(
				medicamento_estoque['pos']['x'],
				medicamento_estoque['pos']['y'],
				medicamento_estoque['pos']['z'],
				medicamento_estoque['pos']['r']
			)

			put_pos = Pos(
				medicamento.pos.x,
				medicamento.pos.y,
				medicamento.pos.z,
				medicamento.pos.r
			)

			for i in range(0, medicamento.quantidade):
				print(f"Montando {medicamento.nome} {i + 1}/{medicamento.quantidade}")
				self.assemble_medication(
					# consider n the quantity of the medicamento (how many will be assembled)
					put_pos.offset_z(i * medicamento.altura), # positive offset multiplied by the index (starts at 0, ends at n)
					get_pos.offset_z(medicamento.quantidade-i * medicamento.altura) # negative offset multiplied by the index (starts at n, ends at 0)

					# this script effectively turns the final get_pos into the one in the config, and the first ones are offset, so the get pos must be obtained thru a empty tower and not a full one

					# the same applies to put_pos, you must register it as the position without any medication (table height) and it will automatically rise to match the height of the current tower that is stacking
				)
				while self.assembling: time.sleep(0.1)
				print("PASS")

		self.robot.home()



	def assemble_medication(self, put_pos: Pos, get_pos: Pos):
		"""
			Recebe um medicamento e monta ele
		"""
		self.assembling = True
		print(f"Montando medicamento {put_pos.x} {put_pos.y} {put_pos.z} {put_pos.r} | {get_pos.x} {get_pos.y} {get_pos.z} {get_pos.r}")
		self.robot.move_safe(get_pos.x, get_pos.y, get_pos.z)

		self.should_stop = True

		pub.subscribe(self.after_qrcode, "camera_data")

		self.robot.move_safe(put_pos.x, put_pos.y, put_pos.z)
		self.should_stop = False

		self.robot.tool("suction", False)

		self.robot.move_safe(put_pos.x, put_pos.y, 80)

	def after_qrcode(self, data: str):
		print(f"QRCODE RECEIVED, CONTINUING ASSEMBLY: {data}")

		self.robot.tool("suction", True)

		pub.unsubscribe(self.after_qrcode, "camera_data")

		self.assembling = False



	def stop_during(self, data: str):
		print(data)
		# if self.should_stop: x