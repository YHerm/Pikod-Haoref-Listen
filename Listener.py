import requests
import json
import time

PIKOD_HAOREF_ALERTS_JSON_URL = "https://www.oref.org.il/warningMessages/alert/Alerts.json"


def fetch_alerts():
    try:
        response = requests.get(PIKOD_HAOREF_ALERTS_JSON_URL)
        response.raise_for_status()

        print("Raw response:", response.text)

        data = json.loads(response.text)
        print("Fetched alerts:", data)
        return data

    except requests.exceptions.RequestException as exception:
        print(f"Request error: {exception}")

    except json.JSONDecodeError as exception:
        print(f"JSON decoding error: {exception}")

    print("No alerts found or error occurred.")
    return None


def track_alerts():
    while True:
        print("**************************")
        fetch_alerts()
        time.sleep(1)


if __name__ == "__main__":
    track_alerts()
