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


class ListarCompra(DataBase):
    def __init__(
        self,
        codigo: str = None,
        valor: float = None,
        data: datetime = None,
        porcentagem: float = None,
        valor_cashback: int = None,
        status_compra: StatusCompra = None,
        cpf: str = None,
    ):
        self.__codigo = codigo
        self.__valor = valor
        self.__data = data
        self.__porcentagem = porcentagem
        self.__valor_cashback = valor_cashback
        self.__status_compra = status_compra
        self.__cpf = cpf

    @property
    def codigo(self):
        return self.__codigo

    @property
    def valor(self):
        return round(float(self.__valor), 2)

    @property
    def data(self):
        return datetime.strftime(self.__data, "%Y-%M-%D")

    @property
    def porcentagem(self):
        return self.__porcentagem

    @property
    def status_compra(self):
        return self.__status_compra

    @property
    def valor_cashback(self):
        return self.__valor_cashback

    @valor_cashback.setter
    def valor_cashback(self, valor_calculado: float):
        if isinstance(valor_calculado, float):
            self.__valor_cashback = round(valor_calculado, 2)

    @property
    def cpf(self):
        return self.__cpf

    def dict(self):
        return {
            key.replace("_ListarCompra__", ""): value
            for key, value in self.__dict__.items()
        }

    @campos_obrigatorios(["cpf"])
    def listar_todos_por_cpf(self, pagina: int, quantidade: int):
        """
        Lista as informações de compras associadas a um revendedor.

        :param str cpf: CPF do revendedor associado a compra.
        :return: Informações da compra.
        :rtype: :class:`database.compra.ListarCompra` ou None
        """
        self.__offset = (pagina - 1) * quantidade
        self.__quantidade = quantidade
        self.query_string = """SELECT CODIGO, VALOR, DATA, PORCENTAGEM, STATUS_COMPRA, CPF
                            FROM COMPRA
                            JOIN REVENDEDOR ON REVENDEDOR.ID_REVENDEDOR = COMPRA.FK_REVENDEDOR_ID_REVENDEDOR
                            JOIN CREDITO ON CREDITO.ID_CREDITO = COMPRA.FK_CREDITO_ID_CREDITO
                            WHERE REVENDEDOR.CPF = %(cpf)s
                            LIMIT %(quantidade)s OFFSET %(offset)s"""
        compras, total = self.find_all(total=True)
        return total, [ListarCompra(**dict(compra)) for compra in compras]

    def listar_todos(self, pagina: int, quantidade: int):
        """
        Lista todas compras da base, paginando o resultado.

        :param int pagina: Offset da página.
        :param int quantidade: Quantidade de compras para listar.
        :return: Compras da base.
        :rtype: list
        """
        self.__offset = (pagina - 1) * quantidade
        self.__quantidade = quantidade
        self.query_string = """SELECT CODIGO, VALOR, DATA, PORCENTAGEM, STATUS_COMPRA
                            FROM COMPRA
                            JOIN REVENDEDOR ON REVENDEDOR.ID_REVENDEDOR = COMPRA.FK_REVENDEDOR_ID_REVENDEDOR
                            JOIN CREDITO ON CREDITO.ID_CREDITO = COMPRA.FK_CREDITO_ID_CREDITO
                            LIMIT %(quantidade)s OFFSET %(offset)s"""
        compras, total = self.find_all(total=True)
        return total, [ListarCompra(**dict(compra)) for compra in compras]
