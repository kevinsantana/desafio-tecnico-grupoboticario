from fastapi import APIRouter, Depends

from cashback_api.rotas.v1 import compra
from cashback_api.rotas.v1 import revendedor
from cashback_api.rotas.v1 import autenticacao

from cashback_api.utils.autenticacao import JWTBearer


v1 = APIRouter()
DEPENDENCIAS = [Depends(JWTBearer())]

v1.include_router(
    revendedor.router,
    prefix="/revendedor",
    dependencies=DEPENDENCIAS,
    tags=["revendedor"],
)

v1.include_router(autenticacao.router, tags=["autenticacao"])

v1.include_router(
    compra.router,
    prefix="/compras",
    dependencies=DEPENDENCIAS,
    tags=["compras"],
)
