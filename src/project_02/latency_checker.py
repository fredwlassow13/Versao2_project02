import requests
from datetime import datetime
from project_02.cache import Cache


GITHUB_API_URL = "https://api.github.com"
cache = Cache()

def check_latency(use_cache=True):
    cache_key = "latency_status"
    if use_cache:
        cached = cache.get(cache_key)
        if cached:
            return cached
    try:
        response = requests.get(GITHUB_API_URL, timeout=7)
        data = {
            "status_code": response.status_code,
            "response_time_ms": response.elapsed.total_seconds() * 1000,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if use_cache:
            cache.set(cache_key, data, ttl=30)
        return data
    except requests.exceptions.Timeout:
        return None
