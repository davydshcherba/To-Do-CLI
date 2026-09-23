import pytest

from utils import storage
from utils.decorators import logger


@pytest.fixture(autouse=True)
def isolated_storage(tmp_path, monkeypatch):
    """Point storage and logs at a temp dir so tests never touch ~/.todo-cli."""
    monkeypatch.setattr(storage, "APP_DIR", tmp_path)
    monkeypatch.setattr(storage, "TASKS_FILE", tmp_path / "tasks.json")
    monkeypatch.setattr(logger, "LOG_DIR", tmp_path / "_log")
    return tmp_path
