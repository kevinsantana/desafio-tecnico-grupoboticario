from fastapi import APIRouter

from cashback_api.rotas.v1 import revendedor


v1 = APIRouter()

v1.include_router(revendedor.router, prefix="/revendedor", tags=["revendedor"])
