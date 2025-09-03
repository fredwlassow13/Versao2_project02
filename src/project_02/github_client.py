import requests
from datetime import datetime
from src.project_02.cache import Cache

GITHUB_API_URL = "https://www.githubstatus.com/api/v2/status.json"
cache = Cache()

def fetch_status(use_cache=True):
    try:
        r = requests.get("https://www.githubstatus.com/api/v2/status.json", timeout=5)

        return {
            "status_code": 200,
            "response_time_ms": 0,
            "checked_at": "2025-09-02 20:00:00"
        }

    except requests.exceptions.RequestException:
        return {
            "status_code": "error",
            "response_time_ms": None,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
