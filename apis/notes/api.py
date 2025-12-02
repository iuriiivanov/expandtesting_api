import allure
import httpx
from config.headers import Headers
from utils.helper import Helper

from apis.notes.endpoints import Endpoints
from apis.notes.models.model import NotesModel
from apis.notes.payloads import Payloads


class Notes(Helper):
    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create note")
    def create_note(self) -> NotesModel:
        response = httpx.post(
            url=self.endpoints.create_note,
            headers=self.headers.auth,
            json=self.payloads.create_note,
        )
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"  # noqa: S101
        self.attach_response(str(response))
        model = NotesModel(**response.json())
        return model
