from typing import List

from modules.robot.classes.Pos import Pos

class Kit:
	class Medicamento:
		def __init__(self, nome: str, quantidade: int, altura: float, pos: Pos):
			self.nome = nome
			self.quantidade = quantidade
			self.altura = altura
			self.pos = pos

	def __init__(self, kit: dict):
		try:
			self.nome = kit['nome']
			self.medicamentos = []
			for medicamento in kit['medicamentos']:
				self.medicamentos.append(self.Medicamento(
					medicamento['nome'],
					medicamento['quantidade'],
					medicamento['altura'],
					Pos(
						medicamento['pos']['x'],
						medicamento['pos']['y'],
						medicamento['pos']['z'],
						medicamento['pos']['r']
					)
				))
		except Exception as e:
			raise Exception(f"Erro ao criar o kit: {e}")

	def to_dict(self):
		kit = {
			'nome': self.nome,
			'medicamentos': []
		}

		for medicamento in self.medicamentos:
			kit['medicamentos'].append({
				'nome': medicamento.nome,
				'quantidade': medicamento.quantidade,
				'altura': medicamento.altura,
				'pos': {
					'x': medicamento.pos.x,
					'y': medicamento.pos.y,
					'z': medicamento.pos.z,
					'r': medicamento.pos.r
				}
			})

		return kit
