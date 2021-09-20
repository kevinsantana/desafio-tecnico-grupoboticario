import pytest
from unittest.mock import patch

from tests.unit.modulos.conftest import Credito, CreditoNaoExiste

from cashback_api.modulos.credito import listar_um
from cashback_api.excecoes.credito import RegraCashbackNaoExisteException



@patch("cashback_api.modulos.credito.listar_um")
@patch("cashback_api.modulos.credito.Credito")
def test_listar_credito_com_sucesso(mock_credito_db, mock_listar_revendedor):
    mock_credito_db.return_value = Credito()
    result = listar_um(id_cashback=Credito().id_credito)
    assert isinstance(result, dict) is True


@patch("cashback_api.modulos.credito.listar_um")
@patch("cashback_api.modulos.credito.Credito")
def test_listar_credito_nao_existe(mock_credito_db, mock_listar_revendedor):
    with pytest.raises(RegraCashbackNaoExisteException):
        mock_credito_db.return_value = CreditoNaoExiste()
        listar_um(id_cashback=CreditoNaoExiste().id_credito)
