import pytest
from unittest.mock import patch

from tests.unit.modulos.conftest import Revendedor

from cashback_api.modulos.autenticacao import verificar_senha
from cashback_api.excecoes.autenticacao import SenhaIncorretaException
from cashback_api.excecoes.revendedor import RevendedorNaoExisteException


revendedor = Revendedor()


@patch("cashback_api.modulos.autenticacao.verificar_senha")
def test_autenticacao_senha_correta(mock_autenticacao):
    assert verificar_senha(cpf=revendedor.cpf, senha=revendedor.senha) is True


@patch("cashback_api.modulos.autenticacao.verificar_senha")
def test_autenticacao_revenvedor_nao_existe(mock_autenticacao):
    with pytest.raises(RevendedorNaoExisteException):
        verificar_senha(cpf="111", senha="000")


@patch("cashback_api.modulos.autenticacao.verificar_senha")
def test_autenticacao_revenvedor_senha_incorreta(mock_autenticacao):
    with pytest.raises(SenhaIncorretaException):
        verificar_senha(cpf=revendedor.cpf, senha="000")
