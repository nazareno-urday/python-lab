import requests
import json

HTTPBIN_ENDPOINT = "https://httpbin.org"

payload = {
    "script_name" : "devops",
    "action" : "CI/CD",
    "headers" : {
        "fork_allow" : True,
        "commit_allow" : False,
        "add_to_stage" : False,
        "create_branch" : True,
        "creators" : ["David", "Mark", "Alex"]
    },
    "version" : "3,1415"
}

response = requests.post(HTTPBIN_ENDPOINT+"/post", json=payload)
response.raise_for_status()

print(json.dumps(response.json(),indent=4))