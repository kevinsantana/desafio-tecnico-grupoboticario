from fastapi import APIRouter, Body, Query, Request

from cashback_api.rotas.v1 import paginacao

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


@router.get(
    "/listar/cpf",
    status_code=200,
    summary="Listar compras de um revendedor",
    # response_model=CriarCompraResponse,
    # responses=CRIAR_COMPRA_DEFAULT_RESPONSES,
)
def listar_cpf(
    request: Request,
    cpf: str = Query(
        "753.187.987-32",
        description="CPF do revendedor associado a compra",
        min_length=11,
        max_length=14,
        regex=r"\d",
    ),
    quantidade: int = Query(10, description="Quantidade de registros de retorno", gt=0),
    pagina: int = Query(1, description="Página atual de retorno", gt=0)
):
    """
    Listar as compras a partir de um cpf de revendedor.
    """
    compras, total = cpr.listar_por_cpf(cpf=cpf, quantidade=quantidade, pagina=pagina)
    return paginacao(compras, quantidade, pagina, total, str(request.url))


@router.get(
    "/listar/",
    status_code=200,
    summary="Listar as compras da base",
    # response_model=CriarCompraResponse,
    # responses=CRIAR_COMPRA_DEFAULT_RESPONSES,
)
def list_all(
    request: Request,
    quantidade: int = Query(10, description="Quantidade de registros de retorno", gt=0),
    pagina: int = Query(1, description="Página atual de retorno", gt=0)
):
    """
    Enpoint para listar as compras da base.
    """
    compras, total = cpr.listar(quantidade=quantidade, pagina=pagina)
    return paginacao(compras, quantidade, pagina, total, str(request.url))
