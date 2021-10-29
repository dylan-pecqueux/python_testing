from flask import session
import pytest

def test_logout_redirect(client, db):
    client.post('/showSummary', data={"email": "john@simplylift.co"})
    response = client.get('/logout')
    assert response.status_code == 302
    assert b"/" in response.data

def test_logout_destory_session(client, db):
    client.post('/showSummary', data={"email": "john@simplylift.co"})
    client.get('/logout')
    with pytest.raises(KeyError):
        session['club']

