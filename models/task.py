class Task:
    def __init__(self, title: str, assigned_to: str, status: str = "Pending"):
        self.title = title
        self.assigned_to = assigned_to  # User's email string
        self._status = status

    @property
    def status(self) -> str:
        return self._status

    def mark_complete(self):
        self._status = "Complete"

    def to_dict(self):
        return {
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["title"], data["assigned_to"], data["status"])

    def __str__(self):
        return f"[{self.status}] {self.title} (Assigned: {self.assigned_to})"