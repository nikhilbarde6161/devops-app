import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Test the home route returns the correct message."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from DevOps GitOps Pipeline!" in response.data


def test_health_route(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data


def test_home_route_method(client):
    """Test that home route only accepts GET."""
    response = client.post('/')
    assert response.status_code == 405  # Method Not Allowed


def test_health_route_method(client):
    """Test that health route only accepts GET."""
    response = client.post('/health')
    assert response.status_code == 405  # Method Not Allowed
