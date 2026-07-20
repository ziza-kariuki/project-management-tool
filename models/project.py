from typing import List
from models.task import Task

class Project:
    def __init__(self, title: str, description: str, due_date: str, tasks: List[Task] = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    @classmethod
    def from_dict(cls, data: dict):
        task_list = [Task.from_dict(t) for t in data.get("tasks", [])]
        return cls(data["title"], data["description"], data["due_date"], task_list)

    def __str__(self):
        return f"Project: {self.title} | Due: {self.due_date} ({len(self.tasks)} Tasks)"