from flask import session

def test_logout_redirect(client, db):
    response = client.get('/logout')
    assert response.status_code == 302
    assert b"/" in response.data

def test_logout_destory_session(client, db):
    auth = client.post('/showSummary', data={"email": "john@simplylift.co"})
    response = client.get('/logout')
    assert session['club'] == None

