import requests
import config

def test_github_authentication(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(config.GITHUB_USER_URL, headers=headers, timeout=10)
        print(f"{config.GITHUB_USER_URL}: status code ({response.status_code})")
        response.raise_for_status()
        data = response.json()
        print(f"Authentication successful, logged in as {data.get('login')}")

    except requests.exceptions.RequestException as error:
        print(f"Authentication failed, error: {error}")


def search_github_repositories(token):
    query = input("\nSearch Github Repositories: ").strip()
    number_of_results = input("How many repositories?: ").strip()

    params = {
        "q": query,
        "sort" : "stars",
        "order" : "desc",
        "per_page" : number_of_results,
        "page" : 1
    }

    headers = {
        "Authorization" : f"Bearer {token}"
    }

    try:
        response = requests.get(config.GITHUB_SEARCH_URL, params=params, headers=headers, timeout=10)
        print(f"\n{config.GITHUB_SEARCH_URL}: status code ({response.status_code})\n")
        response.raise_for_status()
        data = response.json()
        count = 1

        for repos in data.get("items", []):
            print(f"{count}. {repos.get('name')}, stars: {repos.get('stargazers_count')}")
            count += 1

    except requests.exceptions.RequestException as error:
        print(f"Search failed, error: {error}")