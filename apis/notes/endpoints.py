API_BASE_URL = "https://practice.expandtesting.com/notes/api"


class Endpoints:
    """Returns endpoints for note APIs."""

    create_note = f"{API_BASE_URL}/notes"
    get_all_notes = f"{API_BASE_URL}/notes"
    get_note_by_id = lambda self, id: f"{API_BASE_URL}/notes/{id}"  # noqa: E731
    update_existing_note = lambda self, id: f"{API_BASE_URL}/notes/{id}"  # noqa: E731
    update_completed_status_of_note = lambda self, id: f"{API_BASE_URL}/notes/{id}"  # noqa: E731
    delete_note_by_id = lambda self, id: f"{API_BASE_URL}/notes/{id}"  # noqa: E731
