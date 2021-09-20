import pytest
from unittest.mock import patch

from requests.exceptions import ConnectionError

from tests.unit.modulos.conftest import RevendedorListar

from cashback_api.modulos.cashback import recuperar_cashback
from cashback_api.excecoes.cashback import FalhaNaConsultaDoCashback


@patch("requests.get")
@patch("cashback_api.modulos.cashback.recuperar_cashback")
@patch("cashback_api.modulos.cashback.listar_um")
def test_recuperar_cashback_com_sucesso(
    mock_revendedor_db, mock_listar_revendedor, mock_requests_get
):
    mock_revendedor_db.return_value = RevendedorListar().dict()
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json = lambda: {"statusCode": 200, "body": {"credit": 1578}}
    result = recuperar_cashback(id_revendedor=RevendedorListar().id_revendedor)
    assert type(result) is int


@patch("requests.get")
@patch("cashback_api.modulos.cashback.recuperar_cashback")
@patch("cashback_api.modulos.cashback.listar_um")
def test_recuperar_cashback_falha_na_api_externa(
    mock_revendedor_db, mock_requests_get, mock_listar_revendedor
):
    mock_revendedor_db.return_value = RevendedorListar().dict()
    mock_requests_get.return_value = {"statusCode": 500, "body": {"credit": 1578}}
    with pytest.raises(FalhaNaConsultaDoCashback):
        recuperar_cashback(id_revendedor=RevendedorListar().id_revendedor)


@patch("requests.get")
@patch("cashback_api.modulos.cashback.recuperar_cashback")
@patch("cashback_api.modulos.cashback.listar_um")
def test_recuperar_cashback_connection_error(
    mock_revendedor_db, mock_requests_get, mock_listar_revendedor
):
    mock_revendedor_db.return_value = RevendedorListar().dict()
    mock_requests_get.side_effect = ConnectionError()
    with pytest.raises(FalhaNaConsultaDoCashback):
        recuperar_cashback(id_revendedor=RevendedorListar().id_revendedor)
