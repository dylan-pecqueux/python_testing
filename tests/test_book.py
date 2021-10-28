import datetime
from server import loadCompetitions
import server

def test_book_when_competion_in_future(mocker, client):
    date = datetime.datetime.now() + datetime.timedelta(hours=1)
    date = f"{date - datetime.timedelta(microseconds=date.microsecond)}"
    mocker.patch.object(server, 'competitions', [{
            "name": "Summer Festival",
            "date": date,
            "numberOfPlaces": "25"
        }])
    response = client.get('/book/Summer%20Festival/Simply%20Lift')
    assert response.status_code == 200
    assert b"Booking for Summer Festival || GUDLFT" in response.data

def test_book_when_competion_past(mocker, client):
    mocker.patch.object(server, 'competitions', [{
            "name": "Summer Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }])
    response = client.get('/book/Summer%20Festival/Simply%20Lift')
    assert response.status_code == 302
    assert b"/showSummary" in response.data
