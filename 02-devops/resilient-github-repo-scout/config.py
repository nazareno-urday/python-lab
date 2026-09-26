import os
import dotenv

GITHUB_API_BASE = "https://api.github.com"
GITHUB_SEARCH_URL = f"{GITHUB_API_BASE}/search/repositories"
GITHUB_USER_URL = f"{GITHUB_API_BASE}/user"

HTTPBIN_API_BASE = "https://httpbin.org"
HTTPBIN_BASIC_AUTH_URL = f"{HTTPBIN_API_BASE}/basic-auth/myuser/mypsw"
HTTPBIN_POST_URL = f"{HTTPBIN_API_BASE}/post"
HTTPBIN_RETRY_URL = f"{HTTPBIN_API_BASE}/status/200,500,503,404"

def load_github_token():
    dotenv.load_dotenv()
    token = os.getenv("TOKEN")

    try:

        if token is not None:
            return token

        else:
            raise RuntimeError

    except RuntimeError:
        print("\nGithub Token not found")