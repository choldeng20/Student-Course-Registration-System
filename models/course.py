class Course:
    def __init__(self, course_id: str, name: str, trainer: str, capacity: int):
        self.course_id = course_id
        self.name = name
        self.trainer = trainer
        self.capacity = int(capacity)

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "name": self.name,
            "trainer": self.trainer,
            "capacity": self.capacity,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("course_id", ""), d.get("name", ""), d.get("trainer", ""), d.get("capacity", 0))

    def display(self):
        return (
            f"Course ID: {self.course_id}\n"
            f"Course Name: {self.name}\n"
            f"Trainer: {self.trainer}\n"
            f"Capacity: {self.capacity} students"
        )
