import pytest

from bifrost.loadbalancer import loadbalancer

@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_blue(client):
    result = client.get('(/', headers={'Host': 'www.blue.no'})
    assert b'This is the blue application server' in result.data

def test_host_routing_green(client):
    result = client.get('(/', headers={'Host': 'www.green.no'})
    assert b'This is the green application server' in result.data

def test_host_routing_notfound(client):
    result = client.get('(/', headers={'Host': 'www.notfound.no'})
    assert b'Not Found' in result.data
    assert 404 == result.status_code