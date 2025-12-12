import allure
import pytest
import random

from config.base_test import BaseTest


@allure.epic("Notes manipulation")
@allure.feature("Notes")
class TestNotes(BaseTest):
    """TestNotes Class"""

    @pytest.mark.regression
    @allure.title("Create a new note")
    def test_create_note(self) -> None:
        note = self.api_notes.create_note()
        self.api_notes.get_note_by_id(note.data.id)

    @pytest.mark.regression
    @allure.title("Get all notes")
    def test_get_all_notes(self) -> None:
        self.api_notes.get_all_notes()

    @pytest.mark.regression
    @allure.title("Delete a note by ID")
    def test_delete_note_by_id(self) -> None:
        id_to_delete = self.api_notes.get_random_note_id_from_existing()
        self.api_notes.delete_note_by_id(id_to_delete)
        self.api_notes.get_note_by_id__note_not_found(id_to_delete)
