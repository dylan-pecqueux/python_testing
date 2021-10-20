import pytest

from server import app


@pytest.fixture
def client():
    app.config.from_mapping(TESTING=True)
    with app.test_client() as client:
        yield client