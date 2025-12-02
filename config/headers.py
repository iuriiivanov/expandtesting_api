import os
from typing import ClassVar

from dotenv import load_dotenv

load_dotenv()


class Headers:
    auth: ClassVar[dict[str, str]] = {"x-auth-token": f"{os.getenv(key='API_DEFAULT_TOKEN')}"}
