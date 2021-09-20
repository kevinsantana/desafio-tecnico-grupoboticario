from fastapi import APIRouter, Path

from cashback_api.modulos import cashback as info_cashback
from cashback_api.models.cashback import (
    ConsultarCashbackResponse,
    CONSULTAR_CASHBACK_DEFAULT_RESPONSES,
)

router = APIRouter()


@router.get(
    "/{id_revendedor}",
    status_code=200,
    summary="Exibir o acumulado de cashback para um revendedor",
    response_model=ConsultarCashbackResponse,
    responses=CONSULTAR_CASHBACK_DEFAULT_RESPONSES,
)
def exibir_cashback(
    id_revendedor: str = Path(
        1,
        description="Id do revendedor",
        regex=r"\d",
    ),
):
    """
    Acumulado de cashback para um revendedor.
    """
    return {"credito": info_cashback.recuperar_cashback(id_revendedor=id_revendedor)}
