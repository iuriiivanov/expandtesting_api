import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    API_TOKEN: str = os.getenv(key="API_TOKEN", default="API_TOKEN")
    API_BASE_URL: str = os.getenv(key="API_BASE_URL", default="API_BASE_URL")
    HEALTH_CHECK_ENDPOINT: str = os.getenv(key="HEALTH_CHECK_ENDPOINT", default="API_BASE_URL")
