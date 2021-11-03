from flask import session


def test_purchase_two_times(client, db):
    club = db["clubs"]

    connect = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert connect.status_code == 200
    assert session["club"] == "john@simplylift.co"
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert club[0]["points"] == "7"

    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "3"},
    )
    assert club[0]["points"] == "7"
    assert b"Error, you redeem more points or places than available" in response.data
