import requests
from datetime import datetime
from project_02.cache import Cache


GITHUB_API_URL = "https://www.githubstatus.com/api/v2/status.json"
cache = Cache()

def fetch_status(use_cache=True):
    try:
        r = requests.get("https://www.githubstatus.com/api/v2/status.json", timeout=5)

        return {
            "status_code": r.status_code,
            "response_time_ms": r.elapsed.total_seconds() * 1000,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except requests.exceptions.RequestException:
        return {
            "status_code": "error",
            "response_time_ms": None,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
