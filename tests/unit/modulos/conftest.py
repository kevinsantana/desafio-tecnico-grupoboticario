from dataclasses import dataclass


@dataclass()
class Revendedor:
    nome: str = "Isabella Rebeca Agatha Alves"
    cpf: str = "821.218.230-42"
    email: str = "nossoemail@email.com.br"
    senha: str = "123456"

    def existe(self):
        return False

    def inserir(self):
        return True

    def buscar(self):
        return self

    def dict(self):
        return self.__dict__


@dataclass()
class RevendedorRepetido:
    nome: str = "Isabella Rebeca Agatha Alves"
    cpf: str = "821.218.230-42"
    email: str = "nossoemail@email.com.br"
    senha: str = "123456"

    def existe(self):
        return True


@dataclass()
class RevendedorListar:
    id_revendedor: int = 1
    nome: str = "Isabella Rebeca Agatha Alves"
    cpf: str = "821.218.230-42"
    email: str = "nossoemail@email.com.br"
    senha: str = "123456"

    def existe(self):
        return True

    def buscar(self):
        return self

    def dict(self):
        return self.__dict__


@dataclass()
class RevendedorListarNaoExiste:
    nome: str = "Isabella Rebeca Agatha Alves"
    cpf: str = "821.218.230-42"
    email: str = "nossoemail@email.com.br"
    senha: str = "123456"

    def existe(self):
        return False

    def buscar(self):
        return self

    def dict(self):
        return self.__dict__


@dataclass()
class RevendedorBuscarNaoExiste:
    nome: str = "Isabella Rebeca Agatha Alves"
    cpf: str = "821.218.230-42"
    email: str = "nossoemail@email.com.br"
    senha: str = "123456"

    def existe(self):
        return False

    def buscar(self):
        return False

    def dict(self):
        return self.__dict__


@dataclass()
class Credito:
    id_credito: int = 1
    porcentagem: float = 0.10
    ativo: bool = True

    def existe(self):
        return True

    def buscar(self):
        return self

    def dict(self):
        return self.__dict__


@dataclass()
class CreditoNaoExiste:
    id_credito: int = 1
    porcentagem: float = 0.10
    ativo: bool = True

    def existe(self):
        return False
