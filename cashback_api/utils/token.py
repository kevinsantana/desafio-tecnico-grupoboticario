from datetime import datetime, timedelta

import jwt

from cashback_api.config import envs

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.token import (
    TokenExpiradoException,
    TokenInvalidoException,
)


def encode_token(cpf: str):
    payload = {
        "exp": datetime.utcnow() + timedelta(days=0, minutes=30),
        "iat": datetime.utcnow(),
        "scope": "access_token",
        "sub": cpf,
    }
    return jwt.encode(payload, envs.JWT_SECRET, algorithm=envs.JWT_ALGORITHM)


def decode_token(token: str):
    try:
        return jwt.decode(
            token,
            envs.JWT_SECRET,
            algorithms=[envs.JWT_ALGORITHM],
            options={"verify_signature": False},
        )
    except jwt.ExpiredSignatureError:
        raise TokenExpiradoException(
            status=401,
            error="Unauthorized",
            message="Token expirado",
            error_details=[ErrorDetails(message="O token está expirado").to_dict()],
        )
    except jwt.InvalidTokenError:
        raise TokenInvalidoException(
            status=401,
            error="Unauthorized",
            message="Token inválido",
            error_details=[ErrorDetails(message="O token é inválido").to_dict()],
        )
