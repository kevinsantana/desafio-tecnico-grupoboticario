import bcrypt
from base64 import b64encode, b64decode


def hashear_senha(senha_b64: str) -> str:
    """
    Devolve o hash da senha codificada em base64. A senha precisa estar codificada
    em base64.

    :param str senha_b64: Senha codificada em baase64.
    :return: Hash da senha em base64.
    :rtype: str
    """
    return b64encode(bcrypt.hashpw(b64decode(senha_b64), bcrypt.gensalt())).decode(
        "utf-8"
    )


def verificar_hash(hash_b64: str, senha_b64) -> bool:
    """
    Verifica se a senha informada é igual ao hash da senha. A senha e o hash precisam
    estar codificados em base64.

    :param str hash_b64: Hash da senha, codificado em base64.
    :param str senha_b64: Senha codificada em base64.
    :return: Se a senha informada é a mesma do hash.
    :rtyp: bool
    """
    return bcrypt.checkpw(b64decode(senha_b64), b64decode(hash_b64))
