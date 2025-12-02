import httpx
from apis.notes.endpoints import Endpoints
from apis.notes.payloads import Payloads
from config.headers import Headers
from utils.helper import Helper


class Notes(Helper):
    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_note(self) -> None:
        response = httpx.post(
            url=self.endpoints.create_note,
            headers=self.headers.auth,
            json=self.payloads.create_note,
        )
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
