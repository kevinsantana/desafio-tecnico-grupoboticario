from datetime import datetime

from cashback_api.models.compra import StatusCompra
from cashback_api.database import DataBase, campos_obrigatorios


class Compra(DataBase):
    def __init__(
        self,
        codigo: str = None,
        valor: float = None,
        data: datetime = None,
        status_compra: StatusCompra = None,
        fk_revendedor_id_revendedor: int = None,
        fk_credito_id_credito: int = None,
    ):
        self.__codigo = codigo
        self.__valor = valor
        self.__data = data
        self.__status_compra = status_compra
        self.__fk_revendedor_id_revendedor = fk_revendedor_id_revendedor
        self.__fk_credito_id_credito = fk_credito_id_credito

    @property
    def codigo(self):
        return self.__codigo

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return datetime.strftime(self.__data, "%Y-%M-%D")

    @property
    def status_compra(self):
        return self.__status_compra

    @property
    def fk_revendedor_id_revendedor(self):
        return self.__fk_revendedor_id_revendedor

    @property
    def fk_credito_id_credito(self):
        return self.__fk_credito_id_credito

    def dict(self):
        return {
            key.replace("_Compra__", ""): value
            for key, value in self.__dict__.items()
            if value
        }

    @campos_obrigatorios(
        [
            "codigo",
            "valor",
            "data",
            "status_compra",
            "fk_revendedor_id_revendedor",
            "fk_credito_id_credito",
        ]
    )
    def inserir(self):
        """
        Insere uma compra no banco de dados.

        :param str codigo: Código da compra.
        :param float valor: Valor da compra.
        :param datetime data: Data da compra, com ano mês e dia.
        :param str status_compra: Status da compra. Valores válidos: 'Em validação' e 'Aprovada'
        :param int fk_revendedor_id_revendedor: Id do revendedor associado a compra.
        :param int fk_credito_id_credito: Id do cashback vinculado a compra.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = ""
        self.query_string = """INSERT INTO COMPRA (CODIGO, VALOR, DATA,
                            STATUS_COMPRA, FK_REVENDEDOR_ID_REVENDEDOR, FK_CREDITO_ID_CREDITO)
                            values (%(codigo)s, %(valor)s, %(data)s,
                            %(status_compra)s, %(fk_revendedor_id_revendedor)s, %(fk_credito_id_credito)s)"""
        return True if self.insert() else False

    @campos_obrigatorios(["codigo"])
    def existe(self):
        """
        Verifica se uma compra existe no banco de dados.

        :param str codigo: Código da compra.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = (
            "SELECT COUNT(*) FROM COMPRA WHERE COMPRA.CODIGO = %(codigo)s"
        )
        return True if self.find_one()[0] else False

    @campos_obrigatorios(["codigo"])
    def buscar(self):
        """
        Busca um compra no banco de dados a partir do seu código.

        :param str codigo: Código da compra.
        :return: Compra
        :rtype: :class:`database.compra.Compra` ou None
        """
        self.query_string = "SELECT * FROM COMPRA WHERE COMPRA.CODIGO = %(codigo)s"
        compra = self.find_one()
        return Compra(**dict(compra)) if compra else None
