from fastapi import APIRouter, Body

from cashback_api.utils.token import encode_token
from cashback_api.modulos.autenticacao import verificar_senha
from cashback_api.models.autenticacao import (
    LoginRequest,
    LoginResponse,
    LOGIN_DEFAULT_RESPONSES,
)


router = APIRouter()


@router.post(
    "/login",
    status_code=201,
    summary="Realizar login",
    response_model=LoginResponse,
    responses=LOGIN_DEFAULT_RESPONSES,
)
def login(
    dados_login: LoginRequest = Body(..., description="Dados de acesso ao sistema")
):
    if verificar_senha(**dados_login.dict()):
        return {"access_token": encode_token(dados_login.cpf)}
