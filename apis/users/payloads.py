from typing import ClassVar

from faker import Faker

faker = Faker()


class Payloads:
    create_new_user: ClassVar[dict[str, str]] = {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(length=10),
    }
    user_log_in: ClassVar[dict[str, str]] = {
        "email": "test_user@mail.world",
        "password": "test_user#2398476",
    }
    update_user_profile: ClassVar[dict[str, str]] = {
        "email": "test_user@mail.world",
        "password": "test_user#2398476",
    }
    send_password_reset_link: ClassVar[dict[str, str]] = {"email": "test_user@mail.world"}
    verify_password_reset_token: ClassVar[dict[str, str]] = {"token": ""}
    reset_user_password: ClassVar[dict[str, str]] = {"token": "", "newPassword": ""}
    chainge_user_password: ClassVar[dict[str, str]] = {"currentPassword": "", "newPassword": ""}
