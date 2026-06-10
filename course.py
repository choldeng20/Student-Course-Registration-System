import uuid


class Course:
    def __init__(self, title: str, description: str = "", id: str = None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], d.get("description", ""), id=d.get("id"))

    def __repr__(self):
        return f"Course({self.id}, {self.title})"
