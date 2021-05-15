import os

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import initializer, finalizer

from app.core.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def test_app_with_db():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    initializer(
        ["app.models.tortoise"],
        db_url=os.environ.get("DATABASE_TEST_URL"),
    )
    with TestClient(app) as test_client:
        yield test_client
    finalizer()