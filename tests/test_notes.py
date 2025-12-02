from config.base_test import BaseTest


class TestNotes(BaseTest):
    def test_create_note(self) -> None:
        self.api_notes.create_note()
