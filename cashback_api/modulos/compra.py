from datetime import datetime, date

from cashback_api.database.compra import Compra
from cashback_api.modulos.revendedor import _limpa_cpf
from cashback_api.modulos.revendedor import listar_um
from cashback_api.modulos.credito import listar_um as lst_cashback

from cashback_api.excecoes import ErrorDetails
from cashback_api.excecoes.credito import DataInvalidaException

from cashback_api.config import envs


@_limpa_cpf("cpf")
def inserir(*, codigo: str, valor: float, data: datetime, cpf: str):

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

    insercao = Compra(
        codigo=codigo,
        valor=valor,
        data=data,
        status_compra="Aprovado" if cpf == envs.CPF_MASTER else "Em validação",
        fk_revendedor_id_revendedor=revendedor.get("id_revendedor"),
        fk_credito_id_credito=id_regra_cashbak.get("id_credito"),
    ).inserir()
    return True if insercao else False
