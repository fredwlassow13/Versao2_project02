import requests

def get_github_status():
    response = requests.get("https://api.github.com")
    return {
        "status_code": response.status_code,
        "response_time_ms": response.elapsed.total_seconds() * 1000
    }

if __name__ == "__main__":
    status = get_github_status()
    print(f"GitHub API status: {status['status_code']} - Response time: {status['response_time_ms']:.2f} ms")
