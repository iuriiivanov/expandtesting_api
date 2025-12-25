import allure
import pytest
import random

from config.base_test import BaseTest
from apis.notes.payloads import Payloads


@allure.epic("Notes manipulation")
@allure.feature("Notes")
class TestNotes(BaseTest):
    """TestNotes Class"""

    @pytest.mark.regression
    @allure.title("Create a new note")
    @pytest.mark.parametrize(
        "payload",
        [
            Payloads.create_note,
            Payloads.create_note_min_title,
            Payloads.create_note_min_description,
            Payloads.create_note_max_title,
            Payloads.create_note_max_description,
        ],
        ids=[
            "Create a note with default options",
            "Create a note with the shortest title length",
            "Create a note with the shortest description length",
            "Create a note with the longest title length",
            "Create a note with the longest description length",
        ],
    )
    def test_create_note(self, payload: dict[str, str]) -> None:
        note = self.api_notes.create_note(payload)
        self.api_notes.get_note_by_id(note.data.id)

    @pytest.mark.regression
    @allure.title("Get all notes")
    def test_get_all_notes(self) -> None:
        self.api_notes.get_all_notes()

    @pytest.mark.regression
    @allure.title("Get a note by ID")
    def test_get_note_by_id(self) -> None:
        note_created = self.api_notes.create_note(Payloads.create_note)
        note_recieved = self.api_notes.get_note_by_id(note_created.data.id)
        self.api_notes.verify_note_data(note_created.data, note_recieved.data)

    @pytest.mark.regression
    @allure.title("Get a note by ID (404)")
    def test_get_note_by_id_404(self) -> None:
        id = self.api_notes.generate_note_id()
        self.api_notes.get_note_by_id_404(id)

    @pytest.mark.regression
    @allure.title("Update an existing note")
    def test_update_note(self) -> None:
        note = self.api_notes.create_note(Payloads.create_note)
        note_updated = self.api_notes.update_note(note.data.id)
        note_received = self.api_notes.get_note_by_id(note.data.id)
        self.api_notes.verify_note_data(note_updated.data, note_received.data)

    @pytest.mark.regression
    @allure.title("Update the completed status of the note")
    def test_update_completed_status_of_note(self) -> None:
        note = self.api_notes.create_note(Payloads.create_note)
        self.api_notes.change_completed_status_to_true(note.data.id)
        self.api_notes.change_completed_status_to_false(note.data.id)

    @pytest.mark.regression
    @allure.title("Delete a note by ID")
    def test_delete_note_by_id(self) -> None:
        id = self.api_notes.get_random_note_id()
        self.api_notes.delete_note_by_id(id)
        self.api_notes.get_note_by_id_404(id)

    @pytest.mark.regression
    @allure.title("Delete a note by ID (404)")
    def test_delete_note_by_id_404(self) -> None:
        id = self.api_notes.generate_note_id()
        self.api_notes.delete_note_by_id_404(id)

    @pytest.mark.regression
    @allure.title("Delete all note")
    def test_delete_all_notes(self) -> None:
        self.api_notes.delete_all_notes()
