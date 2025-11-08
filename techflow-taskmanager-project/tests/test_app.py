import tempfile
import os
import sqlite3
from src import app, DB_PATH
import pytest

@pytest.fixture
def client(tmp_path, monkeypatch):
    # isolate DB per test
    db_file = tmp_path / "test_tasks.db"
    monkeypatch.setenv("TEST_DB", str(db_file))
    # adjust DB_PATH in module (simple approach)
    from pathlib import Path
    app_path = Path(__file__).resolve().parent.parent / 'tasks.db'
    # ensure app uses tmp db by monkeypatching DB_PATH variable
    from importlib import reload
    import src.app as appmod
    appmod.DB_PATH = db_file
    appmod.init_db()
    with appmod.app.test_client() as client:
        yield client

def test_create_task(client):
    rv = client.post('/task', data={'title':'T1','description':'d'})
    assert rv.status_code == 302  # redirect
    res = client.get('/')
    assert b'T1' in res.data


def test_create_task_invalid(client):
    rv = client.post('/task', data={'title':'','description':'d'})
    assert rv.status_code == 400