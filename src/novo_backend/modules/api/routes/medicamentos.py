from fastapi import APIRouter

from modules.api.classes.Medicamento import Medicamento

router = APIRouter()

@router.get('/{Nome}')
async def read_one(Nome: str):
	return Medicamento.select(Nome)

@router.get('/')
async def read_all():
	return Medicamento.select_all()

@router.post('/')
async def create(medicamento: Medicamento):
	return medicamento.insert()

@router.put('/{Nome}')
async def update(Nome: str, medicamento: Medicamento):
	return medicamento.update(Nome)

@router.delete('/{Nome}')
async def delete(Nome: str):
	return Medicamento.delete(Nome)