from base64 import b64encode

from cashback_api.modulos.revendedor import _limpa_cpf
from cashback_api.database.revendedor import Revendedor
from cashback_api.utils.criptografia import verificar_hash

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.autenticacao import SenhaIncorretaException
from cashback_api.excecoes.revendedor import RevendedorNaoExisteException


@_limpa_cpf("cpf")
def verificar_senha(*, cpf: str, senha: str):
    usuario = Revendedor(cpf=cpf).buscar()
    if not usuario:
        raise RevendedorNaoExisteException(
            status=404,
            error="Not Found",
            message="Revendedor não encontrado",
            error_details=[
                ErrorDetails(message=f"O revendedor {cpf} não existe na base").to_dict()
            ],
        )
    if verificar_hash(usuario.dict().get("senha"), b64encode(bytes(senha, encoding='utf-8')).decode("utf-8")):
        return True
    else:
        raise SenhaIncorretaException(
            status=403,
            error="Forbidden",
            message="Senha incorreta",
            error_details=[
                ErrorDetails(message="A senha informada está incorreta").to_dict()
            ],
        )
