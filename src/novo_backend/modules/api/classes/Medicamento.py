import pydantic

from fastapi.responses import JSONResponse
from tinydb import Query

from modules.api.classes.Pos import Pos
from database.wrapper import DB

class Medicamento(pydantic.BaseModel):
	nome: str
	pos: Pos

	def insert(self):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				if len(medicamentos_db.search(Query().nome == self.nome)) > 0:
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento já cadastrado"
					}, status_code=409)

				medicamentos_db.insert(self.toDict()) # type: ignore

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao cadastrar o medicamento: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamento inserido com sucesso"
		}, status_code=201)

	def update(self, nome: str):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamentos = medicamentos_db.search(Query().nome == nome)
				if len(medicamentos) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento não encontrado"
					}, status_code=404)

				if medicamentos[0]['nome'] != self.nome:
					if len(medicamentos_db.search(Query().nome == self.nome)) > 0:
						return JSONResponse(content={
							"error": True,
							"message": "Nome do medicamento já cadastrado"
						}, status_code=409)
					# se o medicamento existe em algum kit, renomear o medicamento em todos os kits
					with DB('database/archives/kits.json') as kits_db:
						kits = kits_db.search(Query().medicamentos.any(Query().nome == nome))
						for kit in kits:
							medicamentos = kit['medicamentos'] # type: ignore
							for medicamento in medicamentos: # type: ignore
								if medicamento['nome'] == nome: medicamento['nome'] = self.nome
							kits_db.update(kit, Query().nome == kit['nome']) # type: ignore


				medicamentos_db.update(self.toDict(), Query().nome == nome) # type: ignore

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao atualizar o medicamento: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamento atualizado com sucesso"
		}, status_code=200)

	@classmethod
	def delete(cls, Nome: str):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				if len(medicamentos_db.search(Query().nome == Nome)) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento não cadastrado"
					}, status_code=404)

				with DB('database/archives/kits.json') as kits_db:
					kits_com_medicamento = kits_db.search(Query().medicamentos.any(Query().nome == Nome))
					if len(kits_com_medicamento) > 0:
						nomes_kits = [kit['nome'] for kit in kits_com_medicamento] # type: ignore
						return JSONResponse(content={
							"error": True,
							"message": "O medicamento está nos kits: " + ", ".join(nomes_kits) + ", por favor, remova-o(s) do(s) kit(s) antes de deletá-lo" # type: ignore
						}, status_code=409)

				medicamentos_db.remove(Query().nome == Nome)

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao deletar o kit: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Kit deletado com sucesso"
		}, status_code=200)

	@classmethod
	def select(cls, Nome: str):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamento = medicamentos_db.search(Query().nome == Nome)
				if len(medicamento) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento não encontrado"
					}, status_code=404)

				medicamento = medicamento[0]

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao buscar o medicamento: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamento encontrado com sucesso",
			"medicamento": medicamento
		}, status_code=200)

	@classmethod
	def select_all(cls):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamentos = medicamentos_db.all()

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao buscar os medicamentos: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamentos encontrados com sucesso",
			"medicamentos": medicamentos
		}, status_code=200)

	def toDict(self):
		return {
			"nome": self.nome,
			"quantidade": self.quantidade,
			"pos": self.pos.toDict()
		}