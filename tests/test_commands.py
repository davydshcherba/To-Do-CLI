import json

from commands.add_command import add_command
from commands.done_command import done_command
from commands.list_command import list_command
from commands.remove_command import remove_command
from utils import storage


def saved_tasks():
    return json.loads(storage.TASKS_FILE.read_text())


def test_list_reports_no_tasks_when_no_file_exists(capsys):
    list_command()

    assert "No tasks yet" in capsys.readouterr().out


def test_list_reports_no_tasks_when_file_is_blank(capsys):
    storage.TASKS_FILE.write_text("   ")

    list_command()

    assert "No tasks yet" in capsys.readouterr().out


def test_list_prints_each_task_with_done_mark(capsys):
    add_command(text="one")
    add_command(text="two")
    done_command(id=1)
    capsys.readouterr()

    list_command()

    lines = capsys.readouterr().out.splitlines()
    assert lines[0].startswith("[x] 1. one")
    assert lines[1].startswith("[ ] 2. two")


def test_add_assigns_incrementing_ids(capsys):
    add_command(text="one")
    add_command(text="two")

    tasks = saved_tasks()
    assert [t["id"] for t in tasks] == [1, 2]
    assert [t["text"] for t in tasks] == ["one", "two"]
    assert tasks[1]["done"] is False
    assert "Tasks total: 2" in capsys.readouterr().out


def test_add_does_not_reuse_id_of_removed_last_task():
    add_command(text="one")
    add_command(text="two")
    remove_command(id=1)
    add_command(text="three")

    assert [t["id"] for t in saved_tasks()] == [2, 3]


def test_done_marks_task_and_persists(capsys):
    add_command(text="one")

    done_command(id=1)

    assert saved_tasks()[0]["done"] is True
    assert "Task 1 marked as done" in capsys.readouterr().out


def test_done_reports_unknown_id_and_changes_nothing(capsys):
    add_command(text="one")

    done_command(id=99)

    assert saved_tasks()[0]["done"] is False
    assert "Task with id 99 not found" in capsys.readouterr().out


def test_remove_deletes_only_the_matching_task(capsys):
    add_command(text="one")
    add_command(text="two")

    remove_command(id=1)

    assert [t["id"] for t in saved_tasks()] == [2]
    assert "Task 1 removed" in capsys.readouterr().out


def test_remove_reports_unknown_id_and_changes_nothing(capsys):
    add_command(text="one")

    remove_command(id=99)

    assert len(saved_tasks()) == 1
    assert "Task with id 99 not found" in capsys.readouterr().out


def test_legacy_string_done_values_are_converted():
    storage.TASKS_FILE.write_text(json.dumps([
        {"id": 1, "text": "a", "done": "True", "created": "01.01.2025"},
        {"id": 2, "text": "b", "done": "False", "created": "01.01.2025"},
    ]))

    assert [t["done"] for t in storage.load_tasks()] == [True, False]


def test_commands_write_a_log_entry(isolated_storage):
    add_command(text="one")

    logs = list((isolated_storage / "_log").glob("*.json"))
    assert len(logs) == 1
    assert json.loads(logs[0].read_text())[0]["log"] == "add_command"
