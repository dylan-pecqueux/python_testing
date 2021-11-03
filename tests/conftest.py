import datetime
import pytest
import server
from server import app


@pytest.fixture
def client(mocker):
    app.config.from_mapping(TESTING=True)
    with app.test_client() as client:
        yield client


@pytest.fixture
def db(mocker):
    date = datetime.datetime.now() + datetime.timedelta(hours=1)
    date = f"{date - datetime.timedelta(microseconds=date.microsecond)}"
    competitions = mocker.patch.object(
        server,
        "competitions",
        [
            {"name": "Spring Festival", "date": date, "numberOfPlaces": "25"},
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "numberOfPlaces": "13",
            },
            {"name": "Summer Festival", "date": date, "numberOfPlaces": "3"},
        ],
    )
    clubs = mocker.patch.object(
        server,
        "clubs",
        [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
            {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        ],
    )
    return locals()
