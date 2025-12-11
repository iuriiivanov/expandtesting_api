from apis.notes.api_client import Notes


class BaseTest:
    def setup_method(self) -> None:
        self.api_notes = Notes()
