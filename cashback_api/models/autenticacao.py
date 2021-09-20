from pydantic import BaseModel, Field

from cashback_api.excecoes import ErrorDetails
from cashback_api.models import parse_openapi, Message


class LoginRequest(BaseModel):
    cpf: str = Field(
        "000.000.000-00",
        description="CPF utilizado no cadastro",
        min_length=11,
        max_length=14,
        regex=r"\d",
    )
    senha: str = Field(
        ...,
        description="Senha para acessar o sistema",
        min_length=4,
        max_length=72,
    )


class LoginResponse(BaseModel):
    access_token: str


LOGIN_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=404,
            error="Not Found",
            message="Revendedor não encontrado",
            error_details=[
                ErrorDetails(message="O revendedor não existe na base").to_dict()
            ],
        ),
        Message(
            status=403,
            error="Forbidden",
            message="Senha incorreta",
            error_details=[
                ErrorDetails(message="A senha informada está incorreta").to_dict()
            ],
        ),
        Message(
            status=401,
            error="Unauthorized",
            message="Token expirado",
            error_details=[ErrorDetails(message="O token está expirado").to_dict()],
        ),
        Message(
            status=401,
            error="Unauthorized",
            message="Token inválido",
            error_details=[ErrorDetails(message="O token é inválido").to_dict()],
        ),
    ]
)
