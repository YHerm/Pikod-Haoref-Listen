import requests
import json
import time

url = "https://www.oref.org.il/warningMessages/alert/Alerts.json"


def fetch_alerts():
    try:
        response = requests.get(url)
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


if __name__ == "__main__":
    while True:
        print("**************************")
        fetch_alerts()
        time.sleep(1)
