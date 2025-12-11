import allure
import httpx
from config.headers import Headers
from utils.helper import Helper

from apis.notes.endpoints import Endpoints
from apis.notes.models import NoteDeletedModel, NoteModel, NotesModel
from apis.notes.payloads import Payloads


class Notes(Helper):
    def __init__(self) -> None:
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create a new note")
    def create_note(self) -> NoteModel:
        response = httpx.post(
            url=self.endpoints.create_note,
            headers=self.headers.auth,
            json=self.payloads.create_note,
        )
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NoteModel(**response.json())
        return model

    @allure.step("Get all notes")
    def get_all_notes(self) -> NotesModel:
        response = httpx.get(url=self.endpoints.get_all_notes, headers=self.headers.auth)
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NotesModel(**response.json())
        return model

    @allure.step("Get a note by ID")
    def get_note_by_id(self, id: str) -> NoteModel:
        response = httpx.get(url=self.endpoints.get_note_by_id(id), headers=self.headers.auth)
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NoteModel(**response.json())
        return model

    @allure.step("Update an existing note")
    def update_existing_note(self, id: str) -> NoteModel:
        response = httpx.put(
            url=self.endpoints.update_existing_note(id),
            headers=self.headers.auth,
            json=self.payloads.update_existing_note,
        )
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NoteModel(**response.json())
        return model

    @allure.step("Delete a note by ID")
    def delete_note_by_id(self, id: str) -> NoteDeletedModel:
        response = httpx.get(url=self.endpoints.delete_note_by_id(id), headers=self.headers.auth)
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = NoteDeletedModel(**response.json())
        return model
