def test_index_display_points_board(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Simply Lift" in response.data