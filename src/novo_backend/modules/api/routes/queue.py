import json

from fastapi.responses import JSONResponse
from fastapi import APIRouter

from modules.api.classes.Kit import Kit
from modules.api.shared import SharedQueue

router = APIRouter()

@router.get('/{Nome}')
async def add_to_queue(Nome: str):
	queue = SharedQueue.QUEUE

	response = Kit.select(Nome).__dict__
	body = json.loads(response['body'].decode('utf-8'))

	if body['error']: return JSONResponse(content= {
		"error" : True,
		"message": body['message']
	}, status_code=response['status_code'])

	kit = body['kit']
	queue.put(kit)

	return JSONResponse(content={
		"error" : False,
		"message": "Kit adicionado à fila",
		"kit": kit
	}, status_code=response['status_code'])