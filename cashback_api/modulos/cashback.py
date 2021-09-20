import requests
from requests.exceptions import ConnectionError

from cashback_api.config import envs
from cashback_api.modulos.revendedor import listar_um

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.cashback import FalhaNaConsultaDoCashback

from loguru import logger


def recuperar_cashback(id_revendedor: int):
    """
    Acessa a API externa para recuperar o acumulado de cashback para um determinado
    revendedor.

    :param int id_revendedor: Id do revendedor que se deseja recuperar o cashback.
    :raises FalhaNaConsultaDoCashback: Caso a api esteja fora do ar.
    :raises FalhaNaConsultaDoCashback: Se não for possível se conectar com a api.
    :return: Cashback acumulado para o cpf informado.
    :rtype: int
    """
    info_revendedor = listar_um(id_revendedor=id_revendedor)
    url_cashback = (
        f"{envs.ACUMULADO_CASHBACK}/v1/cashback?cpf={info_revendedor.get('cpf')}"
    )
    try:
        req_cashback = requests.get(url=url_cashback)
        if req_cashback.status_code == 200:
            return req_cashback.json().get("body").get("credit")
        else:
            logger.error(f"Falha na consulta da api externa: {req_cashback.json()}")
            raise FalhaNaConsultaDoCashback(
                status=400,
                error="Bad Request",
                message="Falha na consulta do cashback",
                error_details=[
                    ErrorDetails(
                        message="Não foi possível recuperar as informações do cashback no momento"
                    ).to_dict()
                ],
            )
    except ConnectionError as error:
        logger.error(f"Falha de conexão com o serviço externo: {error}")
        raise FalhaNaConsultaDoCashback(
            status=500,
            error="Internal Server Error",
            message="Não é possível consultar o saldo",
            error_details=[
                ErrorDetails(message="Tente acessar o serviço mais tarde").to_dict()
            ],
        )
