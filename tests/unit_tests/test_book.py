def test_book_when_competion_in_future(client, db):
    response = client.get('/book/Summer%20Festival/Simply%20Lift')
    assert response.status_code == 200
    assert b"Booking for Summer Festival || GUDLFT" in response.data

def test_book_when_competion_past(client, db):
    response = client.get('/book/Fall%20Classic/Simply%20Lift')
    assert response.status_code == 302
    assert b"/showSummary" in response.data
