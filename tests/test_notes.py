import allure
import pytest

from config.base_test import BaseTest


@allure.epic("Notes manipulation")
@allure.feature("Notes")
class TestNotes(BaseTest):
    """TestNotes Class"""

    @pytest.mark.regression
    @allure.title("Create a new note")
    def test_create_note(self) -> None:
        note = self.api_notes.create_note()
