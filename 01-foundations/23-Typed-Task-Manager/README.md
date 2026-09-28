# Typed Task Manager

A small Python CLI exercise for managing typed task configurations.

The program creates tasks from configuration dictionaries, shows whether each task is enabled, searches for a task by name, and summarizes the task list.

## What it does

- Defines task data with `TypedDict`.
- Creates `Job` objects from those configurations.
- Stores jobs in a typed list.
- Searches for a job by name, returning a `Job` or `None`.
- Counts total, enabled, and disabled jobs.

**Task execution is simulated.** The program does not perform backups or send reports.

## Example output

```text
backup_database enabled
send_report disabled
{'total': 2, 'enabled': 1, 'disabled': 1}
send_report
```

## Run it

Run the Python file containing the program with Python 3.9 or newer. No external packages are required.

## Concepts practiced

`TypedDict`, `Optional`, typed classes, `list[Job]`, annotated function parameters and return values, and checking for `None` after a search.