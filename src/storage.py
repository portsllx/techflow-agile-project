# storage.py
# Armazenamento simples em memória para simular persistência.
from typing import Dict, Any, List
import itertools

_id_counter = itertools.count(1)
_tasks: Dict[int, Dict[str, Any]] = {}

def list_tasks() -> List[Dict[str, Any]]:
    return list(_tasks.values())

def create_task(title: str, description: str = '', priority: str = 'normal') -> Dict[str, Any]:
    tid = next(_id_counter)
    task = {
        'id': tid,
        'title': title,
        'description': description,
        'done': False,
        'priority': priority
    }
    _tasks[tid] = task
    return task

def get_task(task_id: int) -> Dict[str, Any]:
    return _tasks.get(task_id)

def update_task(task_id: int, **kwargs) -> Dict[str, Any]:
    task = _tasks.get(task_id)
    if not task:
        return None
    task.update(kwargs)
    return task

def delete_task(task_id: int) -> bool:
    return _tasks.pop(task_id, None) is not None

def clear_storage():
    global _tasks, _id_counter
    _tasks = {}
    _id_counter = itertools.count(1)
