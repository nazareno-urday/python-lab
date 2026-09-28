from typing import TypedDict

class Alert(TypedDict):
    id: int
    level : str
    message : str

alerts: list[Alert] = [
    {"id" : 301,
     "level" : "INFO",
     "message": "Changed URL"},

    {"id" : 506,
     "level" : "WARNING",
     "message": "Server closed"},

    {"id" : 403,
     "level" : "ERROR",
     "message": "Client Error"},

    {"id" : 507,
     "level" : "CRITICAL",
     "message": "Server updating"},

    {"id" : 404,
     "level" : "ERROR",
     "message" : "Page not found"}
]

def only_errors(alerts: list[Alert]):
    for alert in alerts:
        if alert["level"] == "ERROR":
            yield alert

for alert in only_errors(alerts):
    print(alert)
