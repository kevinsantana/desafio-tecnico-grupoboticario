from cashback_api.database import DataBase, campos_obrigatorios


class Credito(DataBase):
    def __init__(
        self,
        id_credito: int = None,
        porcentagem: float = None,
        ativo: bool = None,
    ):
        self.__id_credito = id_credito
        self.__porcentagem = porcentagem
        self.__ativo = ativo

    @property
    def id_credito(self):
        return self.__id_credito

    @property
    def porcentagem(self):
        return self.__porcentagem

    @property
    def ativo(self):
        return self.__ativo

    def dict(self):
        return {
            key.replace("_Credito__", ""): value
            for key, value in self.__dict__.items()
            if value
        }

    @campos_obrigatorios(["porcentagem, ativo"])
    def inserir(self):
        """
        Insere uma regra de cashback no banco de dados.

        :param float porcentagem: Uma porcentagem na escala de 0.1 a 1.0 em que a regra
            de cashback se aplica.
        :param bool ativo: Se a regra de cashback está ativa.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = """INSERT INTO CREDITO (PORCENTAGEM, ATIVO) values (%(porcentagem)s, %(ativo)s)"""
        return True if self.insert() else False

    @campos_obrigatorios(["id_credito"])
    def existe(self):
        """
        Verifica se a regra de cashback existe no banco de dados.

        :param str id_credito: Id da regra de cashback.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = (
            """SELECT COUNT(*) FROM CREDITO WHERE CREDITO.ID_CREDITO = %(id_credito)s"""
        )
        return True if self.find_one()[0] else False

    @campos_obrigatorios(["id_credito"])
    def buscar(self):
        """
        Busca uma regra de cashback no banco de dados.

        :param str id_credito: Id da regra de cashback.
        :return: Credito
        :rtype: :class:`database.credito.Credito` ou None
        """
        self.query_string = (
            """SELECT * FROM CREDITO WHERE CREDITO.ID_CREDITO = %(id_credito)s"""
        )
        credito = self.find_one()
        return Credito(**dict(credito)) if credito else None
