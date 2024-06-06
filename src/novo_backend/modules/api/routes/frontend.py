from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.wrapper import DB
from tinydb import Query, TinyDB
from pydantic import BaseModel

router = APIRouter()
templates = Jinja2Templates(directory="templates")

db = TinyDB('database/archives/item.json')

class Item(BaseModel):
    nome: str
    quantidade: int

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name="telaInicial.html", context={"request": request})

@router.get("/telaP", response_class=HTMLResponse)
async def read_page(request: Request):
    kits = []

    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return templates.TemplateResponse("telaP.html", {"request": request, "kits": kits})


@router.get("/deleteKit", response_class=HTMLResponse)
async def read_deleteKit(request: Request):
    return templates.TemplateResponse(name="telaExclusao.html", context={"request": request})

@router.get("/visualizacaoKit", response_class=HTMLResponse)
async def read_visualizacaoKit(request: Request):
    return templates.TemplateResponse(name="visualizacaoKit.html", context={"request": request})

@router.get("/kit", response_class=HTMLResponse)
async def read_kit(request: Request):
    nome_do_kit = request.query_params.get('kit', 'Nome do Kit Não Encontrado')
    medicamentos = []  
    
    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()

            for kit in kits:
                if kit['nome'] == nome_do_kit:
                    medicamentos = kit['medicamentos']
                    break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    return templates.TemplateResponse('kit.html', {"request": request, "nome_do_kit": nome_do_kit, "medicamentos": medicamentos})

@router.get("/telaKit", response_class=HTMLResponse)
async def read_medicamentos(request: Request):
    nome_do_kit = request.query_params.get('kit', 'Nome do Kit Não Encontrado')
    medicamentos = []  
    
    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()

            for kit in kits:
                if kit['nome'] == nome_do_kit:
                    medicamentos = kit['medicamentos']
                    break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    print(nome_do_kit, medicamentos)
    return templates.TemplateResponse('telaKit.html', {"request": request, "nome_do_kit": nome_do_kit, "medicamentos": medicamentos})   

@router.get("/novoKit", response_class=HTMLResponse)
async def read_novoKit(request: Request):
    return templates.TemplateResponse(name="novoKit.html", context={"request": request})

@router.get("/config", response_class=HTMLResponse)
async def read_config(request: Request):
    return templates.TemplateResponse(name="config.html", context={"request": request})

############### ROTAS DO AUXILIAR ####################

@router.get("/auxiliar", response_class=HTMLResponse)
async def read_page(request: Request):

    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    print(kits)

    return templates.TemplateResponse("armazem.html", {"request": request, "kits": kits})

@router.get("/reabastecimento", response_class=HTMLResponse)
async def read_item(request: Request):
    items = []

    try:
          with DB('database/archives/item.json') as items_db:
              items = items_db.all()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return templates.TemplateResponse('reabastecimento.html', {"request": request, "items": items})
  
@router.post("/item")
async def create_item(item: Item):
    # Inserir os dados no banco de dados
    db.insert({'nome': item.nome, 'quantidade': item.quantidade})
    return {"message": "Item criado com sucesso"}
