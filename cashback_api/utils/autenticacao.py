from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from cashback_api.utils.token import decode_token

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.token import (
    TokenInvalidoException,
    TokenNaoInformadoException,
)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credenciais: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credenciais:
            if not decode_token(credenciais.credentials):
                raise TokenInvalidoException(
                    status=403,
                    error="Forbidden",
                    message="O token é inválido",
                    error_details=[
                        ErrorDetails(
                            message="O token é inválido ou está expirado"
                        ).to_dict()
                    ],
                )
            return credenciais.credentials
        else:
            raise TokenNaoInformadoException(
                status=403,
                error="Forbidden",
                message="O token não foi informado",
                error_details=[
                    ErrorDetails(
                        message="O token de autenticação precisa ser informado no cabeçalho da requisição"
                    ).to_dict()
                ],
            )
