def test_index_index(client, db):
    response = client.get('/')
    assert response.status_code == 200

def test_index_display_points_board(client, db):
    response = client.get('/')
    data = response.data.decode()
    print(response.data.decode())
    assert "Simply Lift<br />" in data
    assert "points: 13</br>" in data

def test_index_display_form(client, db):
    response = client.get('/')
    data = response.data.decode()
    assert '<form action="showSummary" method="post">' in data