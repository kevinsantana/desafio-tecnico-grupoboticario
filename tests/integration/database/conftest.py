# import pytest

# from cashback_api.database import DataBase


# class DatabaseTest(DataBase):
#     def dict(self):
#         return {}


# @pytest.fixture(scope='module')
# def setup_module():
#     pass


# @pytest.fixture(scope='module')
# def teardown_module():
#     db = DatabaseTest()
#     db.query_string = "DELETE FROM REVENDEDOR WHERE REVENDEDOR.CPF = '82121823042'"
#     db.insert()


# @pytest.mark.usefixtures("teardown_module")
# def test_tear_down():
#     pass
