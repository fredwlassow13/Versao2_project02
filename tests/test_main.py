import requests
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from project_02.github_client import fetch_status

@patch("project_02.github_client.requests.get")
def test_github_status_returns_expected_keys(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.elapsed.total_seconds.return_value = 0.123
    mock_response.json.return_value = {
        "status_code": 200,
        "response_time_ms": 123,
        "checked_at": "2025-09-02 20:00:00"
    }
    mock_get.return_value = mock_response
    result = fetch_status()

    assert "status_code" in result
    assert "response_time_ms" in result
    assert "checked_at" in result

@patch("project_02.github_client.requests.get")
def test_github_status_values(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 503
    mock_response.elapsed.total_seconds.return_value = 0.435
    mock_response.json.return_value = {
        "status_code": 503,
        "response_time_ms": 435,
        "checked_at": "2025-09-02 20:00:00"
    }
    mock_get.return_value = mock_response
    result = fetch_status()

    assert result["status_code"] == 503
    assert pytest.approx(result["response_time_ms"], rel=1e-2) == 435
    assert len(result["checked_at"]) == 19

@patch("project_02.github_client.requests.get", side_effect=requests.exceptions.RequestException)
def test_github_status_network_exception(mock_get):
    result = fetch_status()
    assert result["status_code"] == "error"


@patch("project_02.github_client.requests.get")
def test_checked_at_format(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.elapsed.total_seconds.return_value = 0.1
    mock_response.json.return_value = {
        "status_code": 200,
        "response_time_ms": 100,
        "checked_at": "2025-09-02 20:00:00"
    }
    mock_get.return_value = mock_response
    result = fetch_status()

    datetime.strptime(result["checked_at"], "%Y-%m-%d %H:%M:%S")
