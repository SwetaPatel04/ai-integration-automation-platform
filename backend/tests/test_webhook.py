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
    - Agent-driven automation metadata
    - Agent decision output
    """

    payload = {
        "source": "pytest",
        "trigger": "webhook-test"
    }

    response = client.post(
        "/webhook/external-trigger",
        json=payload
    )

    # Verify HTTP response code
    assert response.status_code == 200

    data = response.get_json()

    # Updated automation identifier
    assert data["automation"] == "agent-driven-webhook"

    # Agent output validation
    assert "agent_result" in data
    assert data["agent_result"]["decision"] == "approved"
