import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    API_BASE_URL: str = os.getenv(key="API_BASE_URL")  # type: ignore
    HEALTH_CHECK_ENDPOINT: str = os.getenv(key="HEALTH_CHECK_ENDPOINT")  # type: ignore
