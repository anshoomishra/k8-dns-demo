import os
import time

import requests


USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8000/api/users/")
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "5"))


def main():
    while True:
        try:
            response = requests.get(USER_SERVICE_URL, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            print(f"Resolved user-service and received: {response.json()}", flush=True)
        except requests.RequestException as exc:
            print(f"Could not reach {USER_SERVICE_URL}: {exc}", flush=True)
        time.sleep(10)


if __name__ == "__main__":
    main()
