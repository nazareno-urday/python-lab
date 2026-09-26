<div align="center">

# 🛰️ Resilient GitHub Repo Scout

**A modular command-line application for exploring GitHub repositories and learning how reliable API clients are built.**

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GitHub-REST_API-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub REST API">
  <img src="https://img.shields.io/badge/Interface-CLI-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="CLI">
  <img src="https://img.shields.io/badge/HTTP-Requests-FF6F00?style=for-the-badge" alt="HTTP Requests">
</p>

</div>

---

## 📡 About the project

**Resilient GitHub Repo Scout** is a modular Python CLI application that searches GitHub repositories and demonstrates how real HTTP clients authenticate, exchange JSON data, handle failures, enforce timeouts, and retry unsuccessful requests.

The project combines the GitHub REST API with httpbin testing endpoints to provide a controlled environment for exploring both successful requests and common failure scenarios.

Unlike a basic API script that sends one request and terminates, this application includes multiple authentication methods, configurable searches, exception handling, fixed retries, exponential backoff, jitter, and separation of responsibilities across dedicated Python modules.

---

## ✨ Features

### GitHub repository search

- Searches public repositories through the GitHub REST API.
- Accepts custom search terms from the user.
- Allows the user to choose the number of displayed results.
- Sorts repositories by stars in descending order.
- Displays repository names and star counts.
- Uses authenticated requests to improve API access.

### Authentication tests

- Loads a GitHub token securely from a `.env` file.
- Tests GitHub Bearer token authentication.
- Retrieves the username associated with the token.
- Demonstrates HTTP Basic Authentication through httpbin.
- Prevents secrets from being committed to Git.

### Retry strategies

- Retries requests after temporary failures.
- Uses a fixed delay for simple retries.
- Simulates request timeouts with delayed responses.
- Detects client errors and server errors.
- Avoids retrying non-recoverable `4xx` responses.
- Retries temporary `5xx` server failures.
- Implements exponential backoff.
- Adds random jitter to prevent synchronized retries.

### POST and JSON

- Sends structured data using an HTTP `POST` request.
- Automatically serializes Python dictionaries into JSON.
- Uses the `application/json` content type.
- Reads and displays the JSON returned by the server.

---

## 🧠 Concepts demonstrated

This project applies the following Python and HTTP concepts:

- REST API consumption
- HTTP `GET` and `POST` methods
- Query parameters
- Request headers
- Bearer token authentication
- HTTP Basic Authentication
- Environment variables
- JSON serialization and deserialization
- HTTP status codes
- `raise_for_status()`
- Timeouts
- Exception handling
- Fixed retry intervals
- Exponential backoff
- Random jitter
- Modular Python architecture
- Command-line menu navigation

---

## 🏗️ Project structure

```text
resilient-github-repo-scout/
├── main.py
├── cli.py
├── config.py
├── github_client.py
├── httpbin_client.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Module responsibilities

| Module | Responsibility |
|---|---|
| `main.py` | Application entry point |
| `cli.py` | Menus, user input and application flow |
| `config.py` | API endpoints and environment configuration |
| `github_client.py` | GitHub authentication and repository searches |
| `httpbin_client.py` | Basic authentication, POST requests and retry demonstrations |

This separation keeps the interface, configuration and HTTP operations independent and easier to maintain.

---

## 🔄 Application flow

```text
main.py
   │
   ▼
cli.py
   ├── GitHub repository search
   ├── Authentication tests
   ├── Retry tests
   └── POST and JSON test
         │
         ├── github_client.py
         ├── httpbin_client.py
         └── config.py
```

---

## 🛡️ Resilience strategy

The application uses two retry approaches.

### Simple retry

The client retries a failed request using the same delay between attempts:

```text
Attempt 1 → wait 2 seconds
Attempt 2 → wait 2 seconds
Attempt 3 → stop
```

### Exponential backoff with jitter

The waiting time increases after every unsuccessful attempt:

```text
Attempt 1 → approximately 2 seconds
Attempt 2 → approximately 4 seconds
Attempt 3 → stop
```

A small random value called **jitter** is added to each delay. This reduces the chance of multiple clients retrying simultaneously and overwhelming a recovering service.

The conceptual formula is:

```text
delay = base_delay × 2^(attempt - 1) + jitter
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/nazareno-urday/resilient-github-repo-scout.git
cd resilient-github-repo-scout
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🔐 Environment configuration

Create your local `.env` file from the provided example.

Windows:

```bash
copy .env.example .env
```

Linux or macOS:

```bash
cp .env.example .env
```

Open `.env` and replace the example value with your GitHub token:

```env
TOKEN=your_real_github_token
```

The `.env` file is excluded through `../../.gitignore` and must never be committed.

---

## ▶️ Usage

Run the application from the project directory:

```bash
python main.py
```

The main menu will appear:

```text
=== Resilient GitHub Repo Scout ===

Options:
1. Search GitHub Repositories
2. Test Authentication
3. Test Retries
4. POST and JSON
5. Exit
```

### Repository search

Select option `1`, enter a search query and choose the number of repositories:

```text
Search GitHub Repositories: python devops
How many repositories?: 5
```

Example output:

```text
1. awesome-python, stars: 250000
2. system-design-primer, stars: 300000
3. public-apis, stars: 350000
```

### Authentication tests

Select option `2`:

```text
1. Test GitHub Token Authentication
2. Test Basic Authentication
3. Return to Main Menu
```

A successful GitHub authentication displays the username associated with the token.

### Retry tests

Select option `3`:

```text
1. Test Simple Retry
2. Test Exponential Backoff and Jitter
3. Return to Main Menu
```

The application displays every attempt, the received error and the time before the next retry.

### POST and JSON

Select option `4` to send a JSON payload to httpbin and display the data returned by the server.

---

## 🚨 Error handling

The application handles several categories of failure:

| Failure | Behavior |
|---|---|
| Missing GitHub token | Stops safely and displays an explanatory message |
| Invalid authentication | Displays the API authentication error |
| `4xx` response | Reports a client error and stops retrying |
| `5xx` response | Reports a server error and retries |
| Request timeout | Reports the timeout and retries |
| Connection failure | Catches and displays the request error |
| Maximum attempts reached | Stops after the configured limit |

---

## 🔒 Security

- The GitHub token is stored outside the source code.
- `.env` is excluded from version control.
- `.env.example` documents the required variable without exposing credentials.
- Authentication headers are created only when the program runs.
- The token is never printed in the terminal.

Before every commit, verify that `.env` is not tracked:

```bash
git status --short
```

---

## 📦 Dependencies

The project uses two external packages:

```text
requests
python-dotenv
```

Python standard-library modules such as `json`, `random`, `time` and `os` do not require separate installation.

---

## 🚀 Possible future improvements

- Validate search queries and result limits before sending requests.
- Display repository descriptions, languages and URLs.
- Add pagination for larger result sets.
- Save search results to JSON or CSV.
- Add structured logging.
- Create automated tests with `pytest`.
- Reuse a `requests.Session`.
- Read retry limits and delays from configuration.
- Add GitHub Actions for automated checks.

---

## 🎯 Learning outcome

This project was developed as a practical transition from basic Python programs to modular applications that communicate with external services.

It demonstrates how an API client can remain understandable while handling authentication, secrets, JSON data, HTTP failures, timeouts and retry strategies in a structured way.

---

<div align="center">

**Built with Python, Requests and the GitHub REST API.**

</div>