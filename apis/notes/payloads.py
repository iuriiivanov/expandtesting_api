import random

from faker import Faker

faker = Faker()


class Payloads:
    """Returns payloads for note APIs."""

    def __init__(self) -> None:
        self.create_note: dict[str, str] = {
            "title": faker.text(max_nb_chars=100),
            "description": faker.text(max_nb_chars=1000),
            "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
        }
        self.create_note_min_title: dict[str, str] = {
            "title": "TITL",
            "description": faker.text(max_nb_chars=1000),
            "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
        }
        self.create_note_min_description: dict[str, str] = {
            "title": faker.text(max_nb_chars=100),
            "description": "DESC",
            "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
        }
        self.create_note_max_title: dict[str, str] = {
            "title": "Title 100 Title 100 Title 100 Title 100 Title 100 Title 100 Title 100 Title 100 Title 100 Title 100!",
            "description": faker.text(max_nb_chars=1000),
            "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
        }
        self.create_note_max_description: dict[str, str] = {
            "title": faker.text(max_nb_chars=100),
            "description": "Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description 1000 Description!!!",
            "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
        }
        self.update_existing_note: dict[str, str | bool] = {
            "title": faker.sentence(nb_words=5, variable_nb_words=True),
            "description": faker.text(max_nb_chars=50),
            "completed": random.choice([True, False]),  # noqa: S311
            "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
        }
        self.change_completed_status_to_true: dict[str, str | bool] = {"completed": True}
        self.change_completed_status_to_false: dict[str, str | bool] = {"completed": False}
