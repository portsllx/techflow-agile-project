from typing import List, Optional
from src.models import Task

class TaskStorage:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def create(self, title: str, description: str) -> Task:
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def get_all(self) -> List[Task]:
        return self.tasks.copy()
    
    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update(self, task_id: int, title: str = None, description: str = None, completed: bool = None) -> Optional[Task]:
        task = self.get_by_id(task_id)
        if task:
            if title is not None:  # Mudança aqui
                task.title = title
            if description is not None:  # Mudança aqui
                task.description = description
            if completed is not None:
                task.completed = completed
            return task
        return None
    
    
    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False