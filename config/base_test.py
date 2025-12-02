from apis.notes.api import Notes


class BaseTest:
    def setup_method(self) -> None:
        self.api_notes = Notes()
