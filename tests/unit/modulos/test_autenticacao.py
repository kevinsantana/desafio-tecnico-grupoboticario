import pytest
from unittest.mock import patch

from tests.unit.modulos.conftest import RevendedorListar, Revendedor, RevendedorBuscarNaoExiste

from cashback_api.modulos.autenticacao import verificar_senha
from cashback_api.excecoes.autenticacao import SenhaIncorretaException
from cashback_api.excecoes.revendedor import RevendedorNaoExisteException


revendedor = Revendedor()


@patch("cashback_api.modulos.autenticacao.verificar_senha")
@patch("cashback_api.modulos.autenticacao.verificar_hash")
@patch("cashback_api.modulos.autenticacao.Revendedor")
def test_autenticacao_senha_correta(mock_revendedor_db, mock_verificar_hash, mock_autenticacao):
    mock_revendedor_db.return_value = RevendedorListar()
    mock_verificar_hash.return_value = True
    assert verificar_senha(cpf=revendedor.cpf, senha=revendedor.senha) is True


@patch("cashback_api.modulos.autenticacao.verificar_senha")
@patch("cashback_api.modulos.autenticacao.Revendedor")
def test_autenticacao_revenvedor_nao_existe(mock_revendedor_db, mock_autenticacao):
    with pytest.raises(RevendedorNaoExisteException):
        mock_revendedor_db.return_value = RevendedorBuscarNaoExiste()
        verificar_senha(cpf="111", senha="000")


@patch("cashback_api.modulos.autenticacao.verificar_senha")
@patch("cashback_api.modulos.autenticacao.verificar_hash")
@patch("cashback_api.modulos.autenticacao.Revendedor")
def test_autenticacao_revenvedor_senha_incorreta(mock_revendedor_db, mock_verificar_hash, mock_autenticacao):
    with pytest.raises(SenhaIncorretaException):
        mock_revendedor_db.return_value = RevendedorListar()
        mock_verificar_hash.return_value = False
        verificar_senha(cpf=revendedor.cpf, senha="000")
