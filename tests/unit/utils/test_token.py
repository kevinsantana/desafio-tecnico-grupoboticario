import pytest
from time import sleep
from unittest.mock import patch

from cashback_api.utils.token import encode_token, decode_token
from cashback_api.excecoes.token import (
    TokenExpiradoException,
    TokenInvalidoException,
)

token = encode_token("111")


@patch("cashback_api.utils.token.encode_token")
def test_gerar_token_com_sucesso(mock_teste_token):
    assert token is not False


@patch("cashback_api.utils.token.decode_token")
def test_decodificador_token_com_sucesso(mock_teste_token):
    assert type(decode_token(token)) is dict


@patch("cashback_api.utils.token.decode_token")
def test_token_invalido_deve_lancar_excecao(mock_teste_token):
    with pytest.raises(TokenInvalidoException):
        decode_token("587aaa")


@patch("cashback_api.utils.token.decode_token")
def test_token_expirado_deve_lancar_excecao(mock_teste_token):
    token_expirado = encode_token("111", expira=1)
    with pytest.raises(TokenExpiradoException):
        sleep(2)
        decode_token(token_expirado)
