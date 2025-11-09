# tests for task CRUD
import pytest
from src import storage

def setup_function():
    storage.clear_storage()

def test_create_and_get():
    t = storage.create_task('Test 1', 'desc', priority='high')
    assert t['id'] == 1
    fetched = storage.get_task(1)
    assert fetched['title'] == 'Test 1'

def test_update_task():
    storage.create_task('T', '')
    storage.update_task(1, title='T2', done=True)
    t = storage.get_task(1)
    assert t['title'] == 'T2'
    assert t['done'] is True

def test_delete_task():
    storage.create_task('x')
    ok = storage.delete_task(1)
    assert ok
    assert storage.get_task(1) is None

def test_priority_filter():
    storage.create_task('a', priority='low')
    storage.create_task('b', priority='high')
    high = [t for t in storage.list_tasks() if t['priority']=='high']
    assert len(high) == 1
