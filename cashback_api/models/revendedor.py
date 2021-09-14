from pydantic import BaseModel, Field

from cashback_api.excecoes import ErrorDetails
from cashback_api.models import parse_openapi, Message


class CriarRevendedorRequest(BaseModel):
    nome: str = Field(
        "João Augusto Albuquerque",
        description="Nome completo",
        min_length=10,
        max_length=160,
    )
    cpf: str = Field(
        "000.000.000-00",
        description="Cadastro de pessoa física(CPF)",
        min_length=11,
        max_length=14,
        regex=r"\d",
    )
    email: str = Field(
        "seuemail@mail.com", description="Email", min_length=6, max_length=55
    )
    senha: str = Field(
        ...,
        description="Senha para acessar o sistema",
        min_length=4,
        max_length=72,
    )


class CriarRevendedorResponse(BaseModel):
    data: bool


CRIAR_REVENDEDOR_DEFAULT_RESPONSES = parse_openapi(
    [
        Message(
            status=409,
            error="Conflict",
            message="Dado repetido",
            error_details=[
                ErrorDetails(
                    message="Os dados informados para o revendedor já existem na base"
                ).to_dict()
            ],
        ),
    ]
)
