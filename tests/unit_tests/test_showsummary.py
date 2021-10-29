def test_showsummary_when_email_found(client):
    response = client.post('/showSummary', data={"email": "john@simplylift.co"})
    assert response.status_code == 200
    assert b"Summary | GUDLFT Registration" in response.data

def test_showsummary_when_email_not_found(client):
    response = client.post('/showSummary', data={"email": "toto@toto.co"})
    assert response.status_code == 200
    assert b"GUDLFT Registration" in response.data
    assert b"The email isn&#39;t found !" in response.data
