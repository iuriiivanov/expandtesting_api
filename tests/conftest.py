import httpx
import pytest

from config.config import Config as C


@pytest.fixture(scope="session")
def health_check() -> bool:
    response = httpx.get(url=f"{C.API_BASE_URL}/{C.HEALTH_CHECK_ENDPOINT}")

    return response.status_code == 200
