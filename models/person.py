class Person:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "email": self.email, "phone": self.phone}

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("name", ""), d.get("email", ""), d.get("phone", ""))
