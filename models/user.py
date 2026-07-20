class Person:
    """Base class to demonstrate Inheritance"""
    def __init__(self, name: str):
        self._name = name  # Leading underscore implies protected variable

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value


class User(Person):
    """User class inheriting from Person"""
    def __init__(self, name: str, email: str):
        super().__init__(name)
        self._email = email

    @property
    def email(self) -> str:
        return self._email

    def to_dict(self):
        return {"name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["email"])

    def __str__(self):
        return f"User: {self.name} ({self.email})"