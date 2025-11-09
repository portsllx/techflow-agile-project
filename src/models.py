# models.py
# Definição simples de "Model" para tarefas (padrão DTO).
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str = ''
    done: bool = False
    priority: str = 'normal'  # low, normal, high
