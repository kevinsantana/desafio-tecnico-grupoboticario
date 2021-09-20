from pydantic import BaseModel

from cashback_api.excecoes import ErrorDetails
from cashback_api.models import parse_openapi, Message


class ConsultarCashbackResponse(BaseModel):
    credito: int


CONSULTAR_CASHBACK_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=400,
            error="Bad Request",
            message="Falha na consulta do cashback",
            error_details=[
                ErrorDetails(
                    message="Não foi possível recuperar as informações do cashback no momento"
                ).to_dict()
            ],
        ),
        Message(
            status=500,
            error="Internal Server Error",
            message="Não é possível consultar o saldo",
            error_details=[
                ErrorDetails(message="Tente acessar o serviço mais tarde").to_dict()
            ],
        ),
    ]
)
