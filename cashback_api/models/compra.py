from enum import Enum
from datetime import date, datetime
from pydantic import BaseModel, Field

from cashback_api.excecoes import ErrorDetails
from cashback_api.models import parse_openapi, Message


class StatusCompra(str, Enum):
    em_validacao: str = "Em validação"
    aprovado: str = "Aprovado"


class CriarCompraRequest(BaseModel):
    codigo: str = Field(
        "235791113",
        description="Código da compra",
    )
    valor: float = Field(1039.99, description="Valor da compra")
    data: date = Field(
        datetime.utcnow().date(),
        description="Data da compra no formato 2021-09-17",
    )
    cpf: str = Field(
        "000.000.000-00",
        description="CPF do revendedor",
        min_length=11,
        max_length=14,
        regex=r"\d",
    )


class CriarCompraResponse(BaseModel):
    data: bool


CRIAR_COMPRA_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=400,
            error="Bad Request",
            message="Formato de data inválida",
            error_details=[
                ErrorDetails(
                    message="O formato de data é inválida. O formatao correto é 2021-09-17"
                ).to_dict()
            ],
        ),
        Message(
            status=404,
            error="Not found",
            message="Revendedor não existe",
            error_details=[ErrorDetails(message="O revendedor não existe").to_dict()],
        ),
        Message(
            status=404,
            error="Not found",
            message="Regra não existe",
            error_details=[
                ErrorDetails(message="A regra de cashback não existe").to_dict()
            ],
        ),
    ]
)
