"""API endpoint tests"""
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health():
    """Test health check"""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
