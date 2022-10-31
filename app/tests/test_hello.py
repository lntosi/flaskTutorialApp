#!/usr/bin/env python
from app import appbuilder
import pytest
 
@pytest.fixture
def client():
    """ A pytest fixture for test client """
    appbuilder.app.config["TESTING"] = True
    with appbuilder.app.test_client() as client:
        yield client
 
def test_hello(client):
    """ A test method to test view hello """
    resp = client.get("/hello", follow_redirects=True)
    assert 200 == resp.status_code