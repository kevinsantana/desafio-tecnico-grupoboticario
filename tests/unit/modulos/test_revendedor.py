import re
import pytest
from unittest.mock import patch

from tests.unit.modulos.conftest import Revendedor

from cashback_api.modulos.revendedor import inserir, _limpa_cpf
from cashback_api.excecoes.revendedor import RevendedorJaExisteException


@_limpa_cpf("cpf")
def dummy_function(*args, **kwargs):
    return kwargs


@patch("cashback_api.modulos.revendedor._limpa_cpf")
def test_decorator_limpa_cpf(mock_decorator_limpa_cpf):
    funcao = dummy_function(**Revendedor().__dict__)
    assert re.search("[^0-9]", funcao["cpf"]) is not False


@patch("cashback_api.modulos.revendedor.inserir")
def test_inserir_revendedor_com_sucesso(mock_inserir_revendedor):
    assert inserir(**Revendedor().__dict__) is True


@patch("cashback_api.modulos.revendedor.inserir")
def test_inserir_revendedor_repetido(mock_inserir_revendedor):
    with pytest.raises(RevendedorJaExisteException):
        inserir(**Revendedor().__dict__)


# @pytest.mark.usefixtures("teardown_module")
# def test_tear_down():
#     pass
