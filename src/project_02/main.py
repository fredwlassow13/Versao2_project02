import requests

def get_github_status():
    response = requests.get("https://api.github.com")
    return response.status_code

if __name__ == "__main__":
    print("GitHub API status:", get_github_status())
