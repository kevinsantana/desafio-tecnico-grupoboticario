from fastapi.testclient import TestClient

from cashback_api.app import start_application


app = start_application()
client = TestClient(app)
