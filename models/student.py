from .person import Person


class Student(Person):
    def __init__(self, student_id: str, name: str, email: str, phone: str):
        super().__init__(name, email, phone)
        self.student_id = student_id

    def to_dict(self):
        d = super().to_dict()
        d.update({"student_id": self.student_id})
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("student_id", ""), d.get("name", ""), d.get("email", ""), d.get("phone", ""))

    def display(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )
