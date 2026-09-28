from typing import TypedDict, Optional

class JobConfig(TypedDict):
    name: str
    enabled: bool
    owner : Optional[str]

class Job:
    def __init__(self, config: JobConfig) -> None:
        self.name = config["name"]
        self.enabled = config["enabled"]
        self.owner = config["owner"]

    def run(self) -> str:

        if self.enabled:
            return f"{self.name} enabled"

        else:
            return f"{self.name} disabled"

def find_job(name: str, jobs : list[Job]) -> Optional[Job]:
    for job in jobs:
        if job.name == name:
            return job

    return None

def jobs_dict(jobs : list[Job]) -> dict[str,int]:
    total = 0
    enabled = 0
    disabled = 0

    for job in jobs:
        total += 1
        if job.enabled:
            enabled += 1

        else:
            disabled += 1

    return {"total": total,
            "enabled": enabled,
            "disabled": disabled}

backup_config : JobConfig = JobConfig(
    name = "backup_database",
    enabled = True,
    owner = None,
)

report_config : JobConfig = JobConfig(
    name = "send_report",
    enabled = False,
    owner = "Nazareno"
)

job1 = Job(config=backup_config)
job2 = Job(config=report_config)

jobs: list[Job] = [job1, job2]

for job in jobs:
    print(job.run())

print(jobs_dict(jobs))

found_job = find_job("send_report", jobs)

if found_job is not None:
    print(found_job.name)