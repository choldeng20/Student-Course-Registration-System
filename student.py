import uuid


class Student:
    def __init__(self, name: str, email: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.email = email

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["email"], id=d.get("id"))

    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.email})"
