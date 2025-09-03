def parse_official_status(data: dict) -> str:
    indicator = data.get("status", {}).get("indicator", "unknown")
    description = data.get("status", {}).get("description", "No description")
    return f"{indicator.upper()} ({description})"

def parse_latency_status(data):
    return(
        f"[{data['checked_at']}] GitHUB API "
        f"HTTPS {data['status_code']} "
        f"TEMPO: {data['response_time_ms']:.2f} ms"

    )