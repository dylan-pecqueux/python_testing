from datetime import datetime
from server import clubs, competitions

def test_purchacesplace_cant_more_than_12_places(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "13"})
    assert response.status_code == 200
    assert b"Booking for Spring Festival || GUDLFT" in response.data
    assert b"Error, you can&#39;t redeem more than 12 and less than 1" in response.data

def test_purchacesplace_with_pointsclub_available(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"})
    assert response.status_code == 302
    assert b"/showSummary" in response.data

def test_purchacesplace_with_pointsclub_more_than_available(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "12"})
    assert response.status_code == 200
    assert b"Error, you redeem more points or places than available" in response.data
    assert b"Booking for Spring Festival || GUDLFT" in response.data

def test_purchacesplace_deduct_points_club(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"})
    found_club = [club for club in clubs if club['name'] == 'Simply Lift'][0]
    assert response.status_code == 302
    assert b"/showSummary" in response.data
    assert found_club['points'] == 9

def test_purchacesplace_deduct_points_competition(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"})
    found_competition = [comp for comp in competitions if comp['name'] == 'Spring Festival'][0]
    assert response.status_code == 302
    assert b"/showSummary" in response.data
    assert found_competition['numberOfPlaces'] == 19

def test_purchacesplace_cant_input_negative_points(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "-1"})
    assert response.status_code == 200
    assert b"Booking for Spring Festival || GUDLFT" in response.data
    assert b"Error, you can&#39;t redeem more than 12 and less than 1" in response.data

def test_purchacesplace_cant_purchase_more_place_than_available(client):
    response = client.post('/purchasePlaces', data={"competition": "Summer Festival", "club": "Simply Lift", "places": "4"})
    found_competition = [comp for comp in competitions if comp['name'] == 'Summer Festival'][0]
    assert found_competition['numberOfPlaces'] == "3"
    assert response.status_code == 200
    assert b"Booking for Summer Festival || GUDLFT" in response.data
    assert b"Error, you redeem more points or places than available" in response.data
