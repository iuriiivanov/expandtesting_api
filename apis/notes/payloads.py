import random
from typing import ClassVar

from faker import Faker

faker = Faker()


class Payloads:
    """Returns payloads for note APIs."""

    create_note: ClassVar[dict[str, str]] = {
        "title": faker.sentence(nb_words=5, variable_nb_words=True),
        "description": faker.text(max_nb_chars=50),
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }

    update_existing_note: ClassVar[dict[str, str | bool]] = {
        "title": faker.sentence(nb_words=5, variable_nb_words=True),
        "description": faker.text(max_nb_chars=50),
        "completed": random.choice([True, False]),  # noqa: S311
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }

    change_completed_status_to_true: ClassVar[dict[str, str | bool]] = {"completed": True}

    change_completed_status_to_false: ClassVar[dict[str, str | bool]] = {"completed": False}
