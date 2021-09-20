from fastapi import APIRouter, Body

from cashback_api.modulos import revendedor as revd
from cashback_api.models.revendedor import (
    CRIAR_REVENDEDOR_DEFAULT_RESPONSES,
    CriarRevendedorRequest,
    CriarRevendedorResponse,
)

router = APIRouter()


@router.post(
    "/",
    status_code=201,
    summary="Cadastra um revendedor",
    response_model=CriarRevendedorResponse,
    responses=CRIAR_REVENDEDOR_DEFAULT_RESPONSES,
)
def criar(
    revendedor: CriarRevendedorRequest = Body(
        ..., description="Dados básicos para cadastro do revendedor"
    )
):
    """
    Enpoint para criar um novo revendedor.
    """
    return {"data": revd.inserir(**revendedor.dict())}
