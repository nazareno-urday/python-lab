import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

token = os.getenv("TOKEN")
print("Token cargado:", bool(token))

GITHUB_ENDPOINT = "https://api.github.com"
HTTPBIN_ENDPOINT = "https://httpbin.org"

urls = {
    "public" : f"{HTTPBIN_ENDPOINT}",
    "private" : f"{GITHUB_ENDPOINT}/user"
}

"""Basic Authentication:"""

try:
    response = requests.get(urls["public"]+"/basic-auth/myuser/mypsw", auth=("myuser","mypsw"),timeout=5)
    print(f"Requested URL: {urls['public']}")
    response.raise_for_status()
    print(json.dumps(response.json(),indent=4))

except requests.exceptions.HTTPError as error:
    print(f"HTTPError: {error}")

except requests.exceptions.ReadTimeout as error:
    print(f"Timeout: {error}")


"""TOKEN Authentication:"""

new_urls = {
    "public" : f"{GITHUB_ENDPOINT}/zen",
    "private" : f"{GITHUB_ENDPOINT}/user"
}

headers = {
    "Authorization": f"Token {token}"
}

for description, url in new_urls.items():

    try:
        print(f"Requested URL: {url}")
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data.get('name'),indent=4))

    except requests.exceptions.HTTPError as error:
        print(f"HTTPError: {error}")

    except requests.exceptions.JSONDecodeError as error:
        print(f"Couldnt be read as JSON: {response.text[:200]}")