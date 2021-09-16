from dataclasses import dataclass
import pytest

from cashback_api.database import DataBase


@dataclass()
class Revendedor:
    nome: str = "Isabella Rebeca Agatha Alves"
    cpf: str = "821.218.230-42"
    email: str = "nossoemail@email.com.br"
    senha: str = "123456"


class DatabaseTest(DataBase):
    def dict(self):
        return {}


@pytest.fixture(scope='module')
def setup_module():
    pass


@pytest.fixture(scope='module')
def teardown_module():
    print("PASSOU AQUI")
    db = DatabaseTest()
    db.query_string = "DELETE FROM REVENDEDOR WHERE REVENDEDOR.CPF = '82121823042'"
    db.insert()
