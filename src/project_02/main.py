from project_02.github_client import fetch_status
from project_02.latency_checker import check_latency
from project_02.parsers import parse_official_status, parse_latency_status

def main():
    official_data = fetch_status()
    latency_data = check_latency()

    print("Status Oficial:")
    print(parse_official_status(official_data))

    print("Latência da API:")
    print(parse_latency_status(latency_data))

if __name__ == "__main__":
    main()