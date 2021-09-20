from datetime import datetime, date

from cashback_api.database.compra import Compra, ListarCompra

from cashback_api.modulos.revendedor import _limpa_cpf
from cashback_api.modulos.revendedor import listar_um
from cashback_api.modulos.credito import listar_um as lst_cashback

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.credito import DataInvalidaException
from cashback_api.excecoes.compra import CompraJaExisteException

from cashback_api.config import envs


def _formatar_compras(compras: list):
    """
    Formata as compras recuperadas do banco de dados, calculando o cashback para
    a compra e transformando o tipo Decimal para float.

    :param list compras: Lista contendo as compras.
    :return: Lista com as compras formatadas:
    :rtype: list
    """
    data = []
    for compra in compras:
        compra.valor_cashback = compra.valor + (compra.valor * compra.porcentagem)
        data.append(compra.dict())
    return data


@_limpa_cpf("cpf")
def inserir(*, codigo: str, valor: float, data: datetime, cpf: str):
    """
    Insere uma nova compra no banco de dados. Associando a compra a uma porcentagem
    de cashback armazenada no banco de dados.

    ;param str codigo: Codigo da compra
    :param float valor: Valor da compra
    :param datetime data: Data da compra
    :param str cpf: Cpf do revendedor associado a compra.
    :return: Se a compra foi ou não inserida no banco de dados.
    :rtype; bool
    """

    if not isinstance(data, date):
        raise DataInvalidaException(
            status=400,
            error="Bad Request",
            message="Formato de data inválida",
            error_details=[
                ErrorDetails(
                    message=f"O formato de data {data} é inválida. O formatao correto é 2021-09-17"
                ).to_dict()
            ],
        )

    REGRAS_CASHBACK = {valor <= 1000: 1, valor > 1000 <= 1500: 2, valor > 1500: 3}
    revendedor = listar_um(cpf=cpf)
    regra_cashback = REGRAS_CASHBACK.get(True, "Valor inválido")
    id_regra_cashbak = lst_cashback(id_cashback=regra_cashback)

    if Compra(codigo=codigo).existe():
        raise CompraJaExisteException(
            status=409,
            error="Conflict",
            message="Dados repetidos",
            error_details=[
                ErrorDetails(message=f"A compra {codigo} é repetida").to_dict()
            ],
        )

    insercao = Compra(
        codigo=codigo,
        valor=valor,
        data=data,
        status_compra="Aprovado" if cpf == envs.CPF_MASTER else "Em validação",
        fk_revendedor_id_revendedor=revendedor.get("id_revendedor"),
        fk_credito_id_credito=id_regra_cashbak.get("id_credito"),
    ).inserir()
    return True if insercao else False


@_limpa_cpf("cpf")
def listar_por_cpf(*, cpf: str, quantidade: int = 10, pagina: int = 0):
    """
    Lista as compras para um determinado revendedor, paginando o resultado:

    :param str cpf: Cpf do revendedor associado as compras
    :param int quantidade: Quantidade de registros.
    :param pagina: Pagina atual do registro.
    """
    _ = listar_um(cpf=cpf)
    total, compras = ListarCompra(cpf=cpf).listar_todos_por_cpf(pagina, quantidade)
    return _formatar_compras(compras), total


def listar(*, quantidade: int = 10, pagina: int = 0):
    """
    Lista todas as compras, paginando o resultado:

    :param int quantidade: Quantidade de registros.
    :param pagina: Pagina atual do registro.
    """
    total, compras = ListarCompra().listar_todos(pagina, quantidade)
    return _formatar_compras(compras), total
