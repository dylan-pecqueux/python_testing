from flask import session
import pytest


def test_connect_to_logout(client, db):
    club = db["clubs"]
    competitions = db["competitions"]

    connect = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert connect.status_code == 200
    assert session["club"] == "john@simplylift.co"
    assert b"Summary | GUDLFT Registration" in connect.data
    assert b"/book/Summer%20Festival/Simply%20Lift" in connect.data

    book = client.get("/book/Summer%20Festival/Simply%20Lift")
    assert book.status_code == 200
    assert b"Booking for Summer Festival || GUDLFT" in book.data

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert response.status_code == 302
    assert b"/showSummary" in response.data
    assert club[0]["points"] == "7"
    assert competitions[0]["numberOfPlaces"] == "23"

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert club[0]["points"] == "1"
    assert competitions[0]["numberOfPlaces"] == "21"

    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    with pytest.raises(KeyError):
        session["club"]
    assert b"Simply Lift<br />" in response.data
    assert b"points: 1</br>" in response.data
