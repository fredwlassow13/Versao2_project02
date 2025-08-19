import requests
from datetime import datetime

def get_github_status():
    response = requests.get("https://api.github.com"/)
    return {
        "status_code": response.status_code,
        "response_time_ms": response.elapsed.total_seconds() * 1000,
        "checked_at": datetime.now().strfime("%Y-%m-%d %H:%M:%S")
    }

if name == "main":
    status = get_github_status()
    print(f"[{status['checked_at']}] GitHub API status: {status['status_code']} - Response time: {status['response_time_ms']:.2f} ms")
