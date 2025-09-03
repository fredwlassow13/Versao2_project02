from unittest.mock import patch
from project_02.parsers import parse_official_status, parse_latency_status
import requests
import pytest

def test_parse_official_status():
    data = {"status": {"indicator": "none", "description": "All Systems Operational"}}
    result = parse_official_status(data)
    assert result == "NONE (All Systems Operational)"

def test_parse_official_status_missing_fields():
    data = {"status": {}}
    result = parse_official_status(data)
    assert result == "UNKNOWN (No description)"


def test_parse_latency_status():
    data = {
        "checked_at": "2025-09-02 15:40:00",
        "status_code": 200,
        "response_time_ms": 135.022
    }
    result = parse_official_status(data)
    expected = "[2025-09-02 15:40:00] GitHUB API HTTPS 200 TEMPO: 135.022 ms"

def test_parse_latency_status_missing_keys():
    data = {
        "checked_at": "2025-09-02 08:20:00",
        "status_code": 200,
    }
    with pytest.raises(KeyError):
        parse_latency_status(data)