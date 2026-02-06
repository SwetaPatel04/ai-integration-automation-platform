# Import the app factory
from main import create_app


def test_health_endpoint():
    """
    This test verifies that the /health endpoint
    returns a 200 status and expected JSON response.
    """

    # Create Flask app instance
    app = create_app()

    # Use Flask test client
    client = app.test_client()

    # Send GET request to /health
    response = client.get("/health")

    # Assert HTTP status code
    assert response.status_code == 200

    # Assert JSON response content
    json_data = response.get_json()
    assert json_data["status"] == "OK"
