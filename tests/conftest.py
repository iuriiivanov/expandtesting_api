import httpx
import pytest

API_BASE_URL = "https://practice.expandtesting.com/notes/api"


@pytest.fixture(autouse=True, scope="session")
def health_check() -> None:
    response = httpx.get(url=f"{API_BASE_URL}/health-check")
    assert response.status_code == 200
