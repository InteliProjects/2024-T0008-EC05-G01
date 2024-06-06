from fastapi import APIRouter

from modules.api.routes import medicamentos, kits, queue, frontend

router = APIRouter()
router.include_router(medicamentos.router, prefix="/medicamentos")
router.include_router(kits.router, prefix="/kits")
router.include_router(queue.router, prefix="/fila")
router.include_router(frontend.router)