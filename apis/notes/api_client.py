import allure
import httpx
from config.headers import Headers
from utils.helper import Helper

from apis.notes.endpoints import Endpoints
from apis.notes.models import NotesModel
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
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NotesModel(**response.json())
        return model

    @allure.step("Get all notes")
    def get_all_notes(self) -> None:  # list[NotesModel]:
        response = httpx.get(url=self.endpoints.get_all_notes, headers=self.headers.auth)
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        print(response.json())
        # return response.json()

    @allure.step("Get note by ID")
    def get_note_by_id(self, id: str) -> NotesModel:
        response = httpx.get(url=self.endpoints.get_note_by_id(id), headers=self.headers.auth)
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NotesModel(**response.json())
        return model
