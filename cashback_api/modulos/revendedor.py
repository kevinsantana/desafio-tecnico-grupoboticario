import re
import functools
from base64 import b64encode

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.revendedor import CashbackApiException

from cashback_api.database.revendedor import Revendedor
from cashback_api.utils.criptografia import hashear_senha


def _limpa_cpf(cpf):
    def decorator_limpa_cpf(func):
        @functools.wraps(func)
        def wrapper_limpa_cpf(*args, **kwargs):
            kwargs["cpf"] = re.sub("[^0-9]", "", kwargs["cpf"])
            return func(*args, **kwargs)

        return wrapper_limpa_cpf

    return decorator_limpa_cpf


@_limpa_cpf("cpf")
def inserir(*, nome: str, cpf: str, email: str, senha: str):
    """
    Insere um revendedor no banco de dados, verificando se o cpf já existe.

    :param str nome: Nome do revendedor.
    :param str cpf: CPF do revendedor.
    :param str email: Email do revendedor.
    :return: True se o revendedor tiver sido inserido com sucesso, False caso contrário.
    :rtype: bool
    :raises RevendedorJaExisteException: Os dados do revendedor já existem no banco
    de dados.
    """
    if Revendedor(cpf=cpf).existe():
        raise CashbackApiException(
            status=409,
            error="Conflict",
            message="Dados repetidos",
            error_details=[
                ErrorDetails(message=f"O revendedor {cpf} é repetido").to_dict()
            ],
        )
    insercao = Revendedor(
        nome=nome,
        cpf=cpf,
        email=email,
        senha=hashear_senha(b64encode(bytes(senha, encoding="utf-8")).decode("utf-8")),
    ).inserir()
    return True if insercao else False


# @_limpa_cpf("cpf")
# def listar_um(*, cpf: str):
#     """
#     Lista as informações de um usuário no banco de dados.

#     :param str cpf: CPF do usuário buscado.
#     :return: Informações do usuário buscado.
#     :rtype: dict
#     :raises UsuarioInexistenteException: Caso o usuário informado não exista no banco de dados.
#     """
#     if Usuario(cpf=cpf).existe():
#         usuario = ListarUsuario(cpf=cpf).listar_um()
#         usuario.data_nascimento = str(usuario.data_nascimento) if usuario.data_nascimento else usuario.data_nascimento
#         return usuario.dict()
#     else:
#         raise UsuarioInexistenteException(404, cpf)
