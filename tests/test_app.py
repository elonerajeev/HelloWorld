import pytest
import json
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    """Test the main hello world endpoint"""
    response = client.get("/")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["message"] == "Hello, World!"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data
    assert "environment" in data


def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_app_info(client):
    """Test the application info endpoint"""
    response = client.get("/api/info")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["app_name"] == "HelloWorld API"
    assert data["version"] == "1.0.0"
    assert "description" in data
    assert "endpoints" in data
    assert len(data["endpoints"]) == 3


def test_invalid_endpoint(client):
    """Test that invalid endpoints return 404"""
    response = client.get("/invalid")
    assert response.status_code == 404
