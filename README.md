# To-Do CLI

![Tests](https://github.com/davydshcherba/To-Do-CLI/actions/workflows/tests.yml/badge.svg)

A small command-line to-do manager written in Python with no runtime dependencies. Tasks are stored as JSON in your home directory, and every command is logged.

## Features

- `add`, `list`, `done` and `remove` commands through an interactive prompt
- Auto-generated task IDs and creation dates
- Persistent storage in `~/.todo-cli/tasks.json`, so it works from any folder
- Daily action log in `~/.todo-cli/_log/YYYY-MM-DD.json`, written by a `@logger` decorator
- Tolerates a missing or empty data file and converts old `"done": "True"` string values to booleans
- Test suite with pytest and CI on GitHub Actions

## Getting started

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/davydshcherba/To-Do-CLI.git
cd To-Do-CLI
uv run main.py
```

At the prompt, type a command:

```
add, list, done, remove: add
Enter text: Buy milk
Add! Tasks total: 1

add, list, done, remove: list
[ ] 1. Buy milk (23.09.2026)

add, list, done, remove: done
Enter ID: 1
Task 1 marked as done!
```

Press `Ctrl+C` to exit.

## Project structure

```
main.py                    # interactive loop
commands/                  # one module per command (add, list, done, remove)
utils/command_checker.py   # maps input to a command
utils/storage.py           # load/save tasks.json
utils/decorators/logger.py # daily action log
tests/                     # pytest suite
```

## Running the tests

```bash
uv run pytest
```

The tests redirect storage and logs to a temporary directory, so they never touch your real `~/.todo-cli`.

## Data format

```json
[
  {"id": 1, "text": "Buy milk", "done": false, "created": "23.09.2026"}
]
```
