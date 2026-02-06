# pytest is the testing framework used
# Flask provides a test client to simulate requests
import pytest

# Import the app factory from main.py
from main import create_app


@pytest.fixture
def client():
    """
    This fixture creates a test client for the Flask application.
    It runs before each test and provides a clean app instance.
    """
    app = create_app()
    app.testing = True

    # Flask provides a test client that does not require running a server
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """
    Test that the /health endpoint:
    - Returns HTTP 200
    - Returns expected JSON keys and values
    """

    # Simulate a GET request to /health
    response = client.get("/health")

    # Verify HTTP status code
    assert response.status_code == 200

    # Parse JSON response
    data = response.get_json()

    # Core health check
    assert data["status"] == "OK"

    # Application metadata checks
    assert data["app"] == "AI Integration Automation Platform"
    assert "environment" in data