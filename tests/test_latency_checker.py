import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import Timeout
from project_02.latency_checker import check_latency

def test_check_latency():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.elapsed.total_seconds.return_value = 0.243

    with patch("project_02.latency_checker.requests.get", return_value=mock_response):
        result = check_latency(use_cache=False)
        assert result["status_code"] == 200
        assert round(result["response_time_ms"], 2) == 243.0
        assert "checked_at" in result

def test_check_latency_error():
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.elapsed.total_seconds.return_value = 0.253

    with patch("project_02.latency_checker.requests.get", return_value=mock_response):
        result = check_latency(use_cache=False)
        assert result["status_code"] == 500
        assert round(result["response_time_ms"], 2) == 253.0
        assert "checked_at" in result

def test_check_latency_no_found():
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.elapsed.total_seconds.return_value = 0.273

    with patch("project_02.latency_checker.requests.get", return_value=mock_response):
        result = check_latency(use_cache=False)
        assert result["status_code"] == 404
        assert round(result["response_time_ms"], 2) == 273.0
        assert "checked_at" in result

def test_check_latency_timeout():
    with patch("project_02.latency_checker.requests.get", side_effect=Timeout):
        result = check_latency(use_cache=False)
        assert result is None

