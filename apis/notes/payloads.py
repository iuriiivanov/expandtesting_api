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
