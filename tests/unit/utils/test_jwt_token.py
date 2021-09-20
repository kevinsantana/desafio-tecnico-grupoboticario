from tests.unit.utils import client


def test_http_bearer_nao_autenticado_deve_retornar_403():
    response = client.post("/v1/compras/", headers={"Authorization": "Not a cool auth"})
    assert response.json().get("status") == 403


def test_http_bearer_token_invalido_deve_retornar_401():
    response = client.post("/v1/compras/", headers={"Authorization": "Bearer isso nao e uma autenticacao"})
    assert response.json().get("status") == 401


def test_http_bearer_token_nao_informado_deve_retornar_403():
    response = client.post("/v1/compras/", headers={"Authorization": "Bearer"})
    assert response.json().get("status") == 403
