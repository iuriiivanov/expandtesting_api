import httpx
import pytest

from src.config.config import Config as C


def test_health_check() -> None:
    response = httpx.get(url=f"{C.API_BASE_URL}/{C.HEALTH_CHECK_ENDPOINT}")
    assert response.status_code == 200
