from fastapi import APIRouter, Body

from cashback_api.modulos import compra as cpr
from cashback_api.models.compra import (
    CriarCompraRequest,
    CriarCompraResponse,
    CRIAR_COMPRA_DEFAULT_RESPONSES,
)


router = APIRouter()


@router.post(
    "/",
    status_code=201,
    summary="Cadastrar uma compra",
    response_model=CriarCompraResponse,
    responses=CRIAR_COMPRA_DEFAULT_RESPONSES,
)
def criar(
    compra: CriarCompraRequest = Body(
        ..., description="Dados básicos para cadastro de uma nova compra"
    )
):
    """
    Enpoint para criar um nova compra.
    """
    return {"data": cpr.inserir(**compra.dict())}
