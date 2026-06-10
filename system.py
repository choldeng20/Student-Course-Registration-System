import json
from typing import Dict, Set
from student import Student
from course import Course


class RegistrationSystem:
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}
        self.reg_by_student: Dict[str, Set[str]] = {}
        self.reg_by_course: Dict[str, Set[str]] = {}

    # Student operations
    def add_student(self, name: str, email: str) -> Student:
        s = Student(name, email)
        self.students[s.id] = s
        self.reg_by_student.setdefault(s.id, set())
        return s

    def get_all_students(self):
        return list(self.students.values())

    def search_students(self, query: str):
        q = query.lower()
        return [s for s in self.students.values() if q in s.name.lower() or q in s.email.lower()]

    # Course operations
    def add_course(self, title: str, description: str = "") -> Course:
        c = Course(title, description)
        self.courses[c.id] = c
        self.reg_by_course.setdefault(c.id, set())
        return c

    def get_all_courses(self):
        return list(self.courses.values())

    # Registrations
    def register_student(self, student_id: str, course_id: str):
        if student_id not in self.students:
            raise ValueError("Student not found")
        if course_id not in self.courses:
            raise ValueError("Course not found")
        self.reg_by_student.setdefault(student_id, set()).add(course_id)
        self.reg_by_course.setdefault(course_id, set()).add(student_id)

    def get_students_in_course(self, course_id: str):
        ids = self.reg_by_course.get(course_id, set())
        return [self.students[sid] for sid in ids if sid in self.students]

    def get_courses_for_student(self, student_id: str):
        ids = self.reg_by_student.get(student_id, set())
        return [self.courses[cid] for cid in ids if cid in self.courses]

    # Persistence
    def to_dict(self):
        return {
            "students": [s.to_dict() for s in self.students.values()],
            "courses": [c.to_dict() for c in self.courses.values()],
            "reg_by_student": {k: list(v) for k, v in self.reg_by_student.items()},
        }

    @classmethod
    def from_dict(cls, d):
        inst = cls()
        for sd in d.get("students", []):
            s = Student.from_dict(sd)
            inst.students[s.id] = s
            inst.reg_by_student.setdefault(s.id, set())
        for cd in d.get("courses", []):
            c = Course.from_dict(cd)
            inst.courses[c.id] = c
            inst.reg_by_course.setdefault(c.id, set())
        for sid, clist in d.get("reg_by_student", {}).items():
            inst.reg_by_student[sid] = set(clist)
            for cid in clist:
                inst.reg_by_course.setdefault(cid, set()).add(sid)
        return inst

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return cls.from_dict(data)
        except FileNotFoundError:
            return cls()
