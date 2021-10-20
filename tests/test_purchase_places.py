def test_purchacesplace_with_pointsclub_available(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"})
    assert response.status_code == 200
    assert b"Summary | GUDLFT Registration" in response.data
    assert b"Great-booking complete!" in response.data

def test_purchacesplace_with_pointsclub_more_than_available(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "14"})
    assert response.status_code == 200
    assert b"Error, you redeem more points than available" in response.data
    assert b"Summary | GUDLFT Registration" in response.data

def test_purchacesplace_deduct_points_club(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"})
    assert response.status_code == 200
    assert b"Points available: 9" in response.data

def test_purchacesplace_deduct_points_competition(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"})
    assert response.status_code == 200
    assert b"Number of Places: 19" in response.data

def test_purchacesplace_cant_input_negative_points(client):
    response = client.post('/purchasePlaces', data={"competition": "Spring Festival", "club": "Simply Lift", "places": "-1"})
    assert response.status_code == 200
    assert b"Number of Places: 19" in response.data