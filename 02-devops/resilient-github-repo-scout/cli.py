import config
import github_client
import httpbin_client

def show_main_menu():
    print("\n === Resilient GitHub Repo Scout === ")
    print("\nOptions:\n"
          "1. Search Github Repositories\n"
          "2. Test Authentication\n"
          "3. Test Retries\n"
          "4. POST and JSON\n"
          "5. Exit")

    while True:
        option = input("\nPlease select an option: ").strip()

        if option not in ["1", "2", "3", "4", "5"]:
                print("\nInvalid option")

        else:
            return option


def show_authentication_menu():
    print("\nOptions:\n"
          "1. Test Github Token Authentication\n"
          "2. Test Basic Authentication\n"
          "3. Return to Main Menu\n")

    while True:
        option = input("\nPlease select an option: ").strip()

        if option not in ["1", "2", "3"]:
                print("\nInvalid option")

        else:
            return option


def show_retries_menu():
    print("\nOptions:\n"
          "1. Test Simple Retry\n"
          "2. Test Exponential Backoff and Jitter\n"
          "3. Return to Main Menu\n")

    while True:
        option = input("\nPlease select an option: ").strip()

        if option not in ["1", "2", "3"]:
                print("\nInvalid option")
        else:
            return option


def run_cli():
    token = config.load_github_token()

    if token is None:
        return

    while True:
        option = show_main_menu()
        if option == "1":
            print("\nStarting repository search...")
            github_client.search_github_repositories(token)

        elif option == "2":
            print("\n=== Authentication Tests ===")
            choice = show_authentication_menu()

            if choice == "1":
                github_client.test_github_authentication(token)

            elif choice == "2":
                httpbin_client.test_basic_authentication()

        elif option == "3":
            print("\nOpening retries simulator menu...")
            choice = show_retries_menu()

            if choice == "1":
                httpbin_client.test_simple_retry()

            elif choice == "2":
                httpbin_client.test_exponential_backoff()

        elif option == "4":
            print("\nTesting POST and JSON...")
            httpbin_client.test_post_request()

        else:
            print("\nGoodbye!")
            break