import requests
import json
import time

url = "https://www.oref.org.il/warningMessages/alert/Alerts.json"


def fetch_alerts():
    try:
        response = requests.get(url)
        response.raise_for_status()

        print("Raw response:", response.text)

        if not response.text.strip():
            print("No alerts found or error occurred.")
            return None

        data = json.loads(response.text)
        return data

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
    return None


if __name__ == "__main__":
    while True:
        alerts = fetch_alerts()
        if alerts:
            print("Fetched alerts:", alerts)
        else:
            print("No alerts found or error occurred.")

        time.sleep(1)
