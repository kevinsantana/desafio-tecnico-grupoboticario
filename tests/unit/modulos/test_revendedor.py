import re
import pytest
from unittest.mock import patch

from tests.unit.modulos.conftest import (
    Revendedor,
    RevendedorRepetido,
    RevendedorListar,
    RevendedorListarNaoExiste,
)

from cashback_api.modulos.revendedor import inserir, _limpa_cpf, listar_um
from cashback_api.excecoes.revendedor import RevendedorJaExisteException, RevendedorNaoExisteException


@_limpa_cpf("cpf")
def dummy_function(*args, **kwargs):
    return kwargs


@patch("cashback_api.modulos.revendedor._limpa_cpf")
def test_decorator_limpa_cpf(mock_decorator_limpa_cpf):
    funcao = dummy_function(**Revendedor().__dict__)
    assert re.search("[^0-9]", funcao["cpf"]) is not False


@patch("cashback_api.modulos.revendedor.inserir")
@patch("cashback_api.modulos.revendedor.Revendedor")
def test_inserir_revendedor_com_sucesso(mock_revendedor_db, mock_inserir_revendedor):
    mock_revendedor_db.return_value = Revendedor()
    assert inserir(**Revendedor().__dict__)


@patch("cashback_api.modulos.revendedor.inserir")
@patch("cashback_api.modulos.revendedor.Revendedor")
def test_inserir_revendedor_repetido(mock_revendedor_db, mock_inserir_revendedor):
    with pytest.raises(RevendedorJaExisteException):
        mock_revendedor_db.return_value = RevendedorRepetido()
        inserir(**Revendedor().__dict__)


@patch("cashback_api.modulos.revendedor.listar_um")
@patch("cashback_api.modulos.revendedor.Revendedor")
def test_listar_um_com_sucesso(mock_revendedor_db, mock_listar_revendedor):
    mock_revendedor_db.return_value = RevendedorListar()
    result = listar_um(cpf=RevendedorListar().cpf)
    assert isinstance(result, dict) is True


@patch("cashback_api.modulos.revendedor.listar_um")
@patch("cashback_api.modulos.revendedor.Revendedor")
def test_listar_um_revendedor_nao_existe(mock_revendedor_db, mock_listar_revendedor):
    with pytest.raises(RevendedorNaoExisteException):
        mock_revendedor_db.return_value = RevendedorListarNaoExiste()
        listar_um(cpf=RevendedorListar().cpf)
