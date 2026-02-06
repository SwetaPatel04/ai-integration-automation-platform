import pytest
from main import create_app


@pytest.fixture
def client():
    """
    Creates a Flask test client for webhook testing.
    """
    app = create_app()
    app.testing = True

    with app.test_client() as client:
        yield client


def test_webhook_external_trigger(client):
    """
    Test POST /webhook/external-trigger endpoint.
    Validates:
    - Successful response
    - Automation metadata
    - External API data is included
    """

    # Sample webhook payload
    payload = {
        "source": "pytest",
        "trigger": "webhook-test"
    }

    # Send POST request with JSON body
    response = client.post(
        "/webhook/external-trigger",
        json=payload
    )

    # Verify HTTP response code
    assert response.status_code == 200

    # Parse JSON response
    data = response.get_json()

    # Validate automation metadata
    assert data["automation"] == "webhook-triggered"
    assert "event_log" in data
    assert "external_data" in data

    # Validate payload reflection
    assert data["event_log"]["payload"]["source"] == "pytest"
