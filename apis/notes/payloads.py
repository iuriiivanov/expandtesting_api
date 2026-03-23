import random
from typing import ClassVar

from faker import Faker

faker = Faker()


class Payloads:
    """Returns payloads for note APIs."""

    create_note: ClassVar[dict[str, str]] = {
        "title": faker.text(max_nb_chars=100),
        "description": faker.text(max_nb_chars=1000),
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }
    create_note_min_title: ClassVar[dict[str, str]] = {
        "title": "T1$e",
        "description": faker.text(max_nb_chars=1000),
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }
    create_note_min_description: ClassVar[dict[str, str]] = {
        "title": faker.text(max_nb_chars=100),
        "description": "D2#i",
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }
    create_note_max_title: ClassVar[dict[str, str]] = {
        "title": "Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the!",
        "description": faker.text(max_nb_chars=1000),
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }
    create_note_max_description: ClassVar[dict[str, str]] = {
        "title": faker.text(max_nb_chars=100),
        "description": "Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the Lorem Ipsum @2 simply dummy text #3 the printing $4+ typesetting industry. Lorem Ipsum has been the!",
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }
    create_note_all_fields_empty: ClassVar[dict[str, str]] = {
        "title": "",
        "description": "",
        "category": "",
    }
    create_note_all_fields_spaces: ClassVar[dict[str, str]] = {
        "title": "               ",
        "description": "                    ",
        "category": "     ",
    }
    update_existing_note: ClassVar[dict[str, str | bool]] = {
        "title": faker.sentence(nb_words=5, variable_nb_words=True),
        "description": faker.text(max_nb_chars=50),
        "completed": random.choice([True, False]),  # noqa: S311
        "category": random.choice(["Home", "Work", "Personal"]),  # noqa: S311
    }
    change_completed_status_to_true: ClassVar[dict[str, str | bool]] = {"completed": True}
    change_completed_status_to_false: ClassVar[dict[str, str | bool]] = {"completed": False}
