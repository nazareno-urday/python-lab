import json
import random
import time
import requests
import config

def test_basic_authentication():
    user = "myuser"
    password = "mypsw"

    try:
        response = requests.get(config.HTTPBIN_BASIC_AUTH_URL, auth=(user, password), timeout=10)
        print(f"{config.HTTPBIN_BASIC_AUTH_URL}: status code ({response.status_code})")
        response.raise_for_status()
        data = response.json()
        print(f"Authentication: {data.get('authenticated')}, logged in as {data.get('user')}")

    except requests.exceptions.RequestException as error:
        print(f"Authentication failed, error: {error}")


def test_simple_retry():
    max_retries = 4
    delay = 2

    for retry in range(1, max_retries + 1):

        try:
            print(f"attempt: {retry}/{max_retries}")
            response = requests.get(config.HTTPBIN_RETRY_URL, timeout=2)
            response.raise_for_status()
            print(f"Successful response: {response.status_code}")
            break

        except requests.exceptions.Timeout as error:
            print("Request timed out")

        except requests.exceptions.HTTPError as error:

            if error.response.status_code < 500:
                print(f"Failed with client error: {error.response.status_code}")
                break

            else:
                print(f"Failed with server error: {error.response.status_code}")

        except requests.exceptions.RequestException as error:
            print(f"Failed with request error: {error}")

        if retry < max_retries:
            print(f"Trying again in {delay} seconds...")
            time.sleep(delay)

    else:
        print(f"All {max_retries} attempts failed.")


def test_exponential_backoff():
    max_retries = 3
    base_delay = 2

    for retry in range(1, max_retries + 1):

        try:
            print(f"attempt: {retry}/{max_retries}")
            response = requests.get(config.HTTPBIN_RETRY_URL, timeout=10)
            response.raise_for_status()
            print(f"Successful response: {response.status_code}")
            break

        except requests.exceptions.HTTPError as error:

            if error.response.status_code < 500:
                print(f"Failed with client error: {error.response.status_code}")
                break

            else:
                print(f"Failed with server error: {error.response.status_code}")

        except requests.exceptions.RequestException as error:
            print(f"Failed with request error: {error}")

        if retry < max_retries:
            exponential_delay = base_delay * (2 ** (retry - 1))
            jitter = random.uniform(0, 1)
            delay = exponential_delay + jitter

            print(f"Trying again in {round(delay,2)} seconds...")
            time.sleep(delay)

    else:
        print(f"All {max_retries} attempts failed.")


def test_post_request():
    payload = {
        "project" : "Resilient GitHub Repo Scout",
        "status" : "testing",
        "owner" : "Nazareno"
    }

    try:
        response = requests.post(config.HTTPBIN_POST_URL, json=payload, timeout=10)
        print(f"{config.HTTPBIN_POST_URL}: status code ({response.status_code})")
        response.raise_for_status()

        data = response.json()
        print(f"\nHere is the data that you sent:\n{json.dumps(data.get('json'), indent=4)}")

    except requests.exceptions.RequestException as error:
        print("An error occurred: ", error)