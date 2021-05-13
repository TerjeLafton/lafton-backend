import os

import pytest
from fastapi.testclient import TestClient

from app import main
from app.core.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=True, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client
