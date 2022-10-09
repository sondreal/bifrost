import pytest

from bifrost.loadbalancer import loadbalancer

@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_hello(client):
    result = client.get('/')
    assert b'hello' in result.data
