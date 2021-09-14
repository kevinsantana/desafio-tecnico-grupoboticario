from cashback_api.database import DataBase, campos_obrigatorios


class Revendedor(DataBase):
    def __init__(
        self,
        id_revendedor: int = None,
        nome: str = None,
        cpf: str = None,
        email: str = None,
        senha: str = None
    ):
        self.__id_revendedor = id_revendedor
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha

    @property
    def id_revendedor(self):
        return self.__id_revendedor

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    def dict(self):
        return {
            key.replace("_Revendedor__", ""): value
            for key, value in self.__dict__.items()
            if value
        }

    @campos_obrigatorios(["nome", "cpf", "email", "senha"])
    def inserir(self):
        """
        Insere um usuário no banco de dados.

        :param str nome: Nome do revendedor
        :param str cpf: CPF do revendedor
        :param str email: Email do revendedor
        :param str: Senha de acesso ao sistema
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = ""
        self.query_string = """INSERT INTO REVENDEDOR (NOME, CPF, EMAIL, SENHA)
        values (%(nome)s, %(cpf)s, %(email)s, %(senha)s)"""
        return True if self.insert() else False

    @campos_obrigatorios(["cpf"])
    def existe(self):
        """
        Verifica se um revendedor existe no banco de dados.

        :param str cpf: CPF do revendedor
        :param str id_revendedor: Id do revendedor no banco de dados.
        :return: True se a operação for exeutada com sucesso, False caso contrário.
        :rtype: bool
        """
        self.query_string = "SELECT COUNT(*) FROM REVENDEDOR WHERE REVENDEDOR.CPF = %(cpf)s"
        if self.__id_revendedor:
            self.query_string += " OR REVENDEDOR.ID_REVENDEDOR = %(id_revendedor)s"
        return True if self.find_one()[0] else False

    @campos_obrigatorios(["cpf"])
    def buscar(self):
        """
        Busca revendedor no banco de dados a partir do cpf ou id do revendedor.

        :param str cpf: CPF do revendedor
        :return: Id do revendedor
        :rtype: dict
        """
        self.query_string = "SELECT * FROM REVENDEDOR WHERE REVENDEDOR.CPF = %(cpf)s"
        if self.__id_revendedor:
            self.query_string += " OR REVENDEDOR.ID_REVENDEDOR = %(id_revendedor)s"
        return self.find_one()
