def test_purchacesplace_cant_more_than_12_places(client, db):
    club = db["clubs"]
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "13"},
    )
    assert response.status_code == 200
    assert club[0]["points"] == "13"
    assert b"Booking for Spring Festival || GUDLFT" in response.data
    assert b"Error, you can&#39;t redeem more than 12 and less than 1" in response.data


def test_purchacesplace_with_pointsclub_available(client, db):
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert response.status_code == 302
    assert b"/showSummary" in response.data


def test_purchacesplace_with_pointsclub_more_than_available(client, db):
    club = db["clubs"]
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Iron Temple", "places": "6"},
    )
    assert response.status_code == 200
    assert b"Error, you redeem more points or places than available" in response.data
    assert b"Booking for Spring Festival || GUDLFT" in response.data
    assert club[1]["points"] == "4"


def test_purchacesplace_deduct_points_club(client, db):
    club = db["clubs"]
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert response.status_code == 302
    assert b"/showSummary" in response.data
    assert club[0]["points"] == "7"


def test_purchacesplace_deduct_points_competition(client, db):
    competitions = db["competitions"]
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert response.status_code == 302
    assert b"/showSummary" in response.data
    assert competitions[0]["numberOfPlaces"] == "23"


def test_purchacesplace_cant_input_negative_points(client, db):
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "-1"},
    )
    assert response.status_code == 200
    assert b"Booking for Spring Festival || GUDLFT" in response.data
    assert b"Error, you can&#39;t redeem more than 12 and less than 1" in response.data


def test_purchacesplace_cant_purchase_more_place_than_available(client, db):
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Summer Festival", "club": "Simply Lift", "places": "4"},
    )
    assert response.status_code == 200
    assert b"Booking for Summer Festival || GUDLFT" in response.data
    assert b"Error, you redeem more points or places than available" in response.data
