from cashback_api.database.credito import Credito

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.credito import RegraCashbackNaoExisteException


def listar_um(*, id_cashback: int):
    """
    Lista as informações de uma regra de cashback.

    :param int id_cashback: Id da regra buscada.
    :return: Regra de cashback aplicada.
    :rtype: dict
    :raises RegraCashbackNaoExisteException: O id da regra não existe.
    """
    if Credito(id_credito=id_cashback).existe():
        return Credito(id_credito=id_cashback).buscar().dict()
    else:
        raise RegraCashbackNaoExisteException(
            status=404,
            error="Not found",
            message="Regra não existe",
            error_details=[
                ErrorDetails(message="A regra de cashback não existe").to_dict()
            ],
        )
