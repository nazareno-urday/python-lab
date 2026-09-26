import requests
import json

GITHUB_ENDPOINT = "https://api.github.com"
HTTPBIN_ENDPOINT = "https://httpbin.org"

"The params were get in REST API"
query = {
    "q" : "AI",
    "sort" : "forks",
    "order" : "desc",
    "per_page" : "10",
    "page" : "1"
}

response = requests.get(GITHUB_ENDPOINT+"/search/repositories", params=query, timeout=5)
print(f"The status code is: {response.status_code}") # If status code 2xx we have been accepted

"""
Different ways to represent the data
print(f"This is the text: {response.text}")
print(f"This is the content: {response.content}")
print(f"This is the json: {response.json()}")
"""

data = response.json()
#print(json.dumps(data, indent=4))

#for description, key in data.items():
    #print(f"{description}: {key}")

# Or even more structured
#print(json.dumps(response.json(), indent=4))

print(f"Repositories found: {data['total_count']}. This are the top 10 repos sorted by forks count:")
for repository in data.get("items"):
    print(f"{repository.get('name')}, forks: {repository.get('forks_count')}")

print(f"{json.dumps(data.get('items')[0], indent=4)}") # Returns the items and values of the top 1 repo