import requests
import json

GITHUB_ENDPOINT = "https://api.github.com"

urls = {
    "permitted_url" : f"{GITHUB_ENDPOINT}/zen",
    "non_permitted_url" : f"{GITHUB_ENDPOINT}/nonexistingurl",
}

for url in urls.values():
    print(f"Requested: {url}")

    try:
        response = requests.get(url, timeout=5)
        print(f"Status code: ({response.status_code})")
        response.raise_for_status()

    except requests.exceptions.HTTPError as error:
        print(f"{url}: {error}")

        try:
            print("error details:")
            print(json.dumps(error.response.json(), indent=4))

        except requests.exceptions.JSONDecodeError:
            print(f"error details: {response.text[:200]}")

    except requests.exceptions.RequestException as error:
        print(f"Failed: {error}")