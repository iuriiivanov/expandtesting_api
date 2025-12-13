import random

import allure
import httpx
from config.headers import Headers
from utils.tools import Helper

from apis.notes.endpoints import Endpoints
from apis.notes.models import DeleteNote200Model, Note404Model, NoteModel, NotesModel
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

    @allure.step("Get a note by ID (404)")
    def get_note_by_id_404(self, id: str) -> Note404Model:
        response = httpx.get(url=self.endpoints.get_note_by_id(id), headers=self.headers.auth)
        assert response.status_code == 404, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = Note404Model(**response.json())
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
    def delete_note_by_id(self, id: str) -> DeleteNote200Model:
        response = httpx.delete(url=self.endpoints.delete_note_by_id(id), headers=self.headers.auth)
        assert response.status_code == 200, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = DeleteNote200Model(**response.json())
        return model

    @allure.step("Delete a note by ID (no notes available)")
    def delete_note_by_id_404(self, id: str) -> Note404Model:
        response = httpx.delete(url=self.endpoints.delete_note_by_id(id), headers=self.headers.auth)
        assert response.status_code == 404, f"Something goes wrong!\n {response.json()}"
        self.attach_response(response.json())
        model = Note404Model(**response.json())
        return model

    @allure.step("Get random note ID")
    def get_random_note_id(self) -> str:
        notes = self.get_all_notes().model_dump()
        assert notes, f"Current user doesn't have any note at the moment!\n{notes}"
        ids = []
        for item in notes["data"]:
            ids.append(item["id"])
        self.attach_value(f"IDs: {ids}")
        return str(random.choice(ids))  # noqa: S311 #

    @allure.step("Generate note ID")
    def generate_note_id(self) -> str:
        random_id = "".join(random.choice("0123456789abcdef") for _ in range(24))  # noqa: S311
        assert self.get_note_by_id_404(random_id), (
            f"ID {random_id} is already in use!\nGenerate another one!"
        )
        self.attach_value(f"Generated ID: {random_id}")
        return random_id

    @allure.step("Delete all notes")
    def delete_all_notes(self) -> None:
        notes = self.get_all_notes().model_dump()
        if notes:
            ids = []
            for item in notes["data"]:
                ids.append(item["id"])
            for id in range(len(ids)):
                self.delete_note_by_id(ids[id])
        notes = self.get_all_notes().model_dump()
        assert notes, f"Note list is not empty!\n{notes}"
        self.attach_value(f"IDs of the deleted notes:\n{ids}")
