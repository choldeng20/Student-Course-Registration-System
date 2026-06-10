import json
import os
from typing import Dict, Set
from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self, data_dir: str = "data"):
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}
        self.reg_by_student: Dict[str, Set[str]] = {}
        self.reg_by_course: Dict[str, Set[str]] = {}
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    # Validation helpers
    def _validate_student_fields(self, student_id, name, email, phone):
        if not student_id:
            raise ValueError("Student ID is required")
        if not name:
            raise ValueError("Student name is required")
        if "@" not in email:
            raise ValueError("Invalid email")
        if not phone:
            raise ValueError("Phone number is required")

    def _validate_course_fields(self, course_id, name, trainer, capacity):
        if not course_id:
            raise ValueError("Course ID is required")
        if not name:
            raise ValueError("Course name is required")
        try:
            cap = int(capacity)
        except Exception:
            raise ValueError("Capacity must be a number")
        if cap <= 0:
            raise ValueError("Capacity must be greater than 0")

    # Student operations
    def add_student(self, student_id: str, name: str, email: str, phone: str):
        self._validate_student_fields(student_id, name, email, phone)
        if student_id in self.students:
            raise ValueError("Duplicate student ID")
        s = Student(student_id, name, email, phone)
        self.students[student_id] = s
        self.reg_by_student.setdefault(student_id, set())
        return s

    def get_all_students(self):
        return list(self.students.values())

    def find_student_by_id(self, student_id: str):
        return self.students.get(student_id)

    def search_students(self, query: str):
        q = query.lower()
        return [s for s in self.students.values() if q in s.name.lower() or q in s.student_id.lower()]

    # Course operations
    def add_course(self, course_id: str, name: str, trainer: str, capacity: int):
        self._validate_course_fields(course_id, name, trainer, capacity)
        if course_id in self.courses:
            raise ValueError("Duplicate course ID")
        c = Course(course_id, name, trainer, int(capacity))
        self.courses[course_id] = c
        self.reg_by_course.setdefault(course_id, set())
        return c

    def get_all_courses(self):
        return list(self.courses.values())

    def find_course_by_id(self, course_id: str):
        return self.courses.get(course_id)

    # Registration operations
    def register_student_to_course(self, student_id: str, course_id: str):
        if student_id not in self.students:
            raise ValueError("Student not found")
        if course_id not in self.courses:
            raise ValueError("Course not found")
        if course_id in self.reg_by_student.get(student_id, set()):
            raise ValueError("Student already registered for this course")
        if len(self.reg_by_course.get(course_id, set())) >= self.courses[course_id].capacity:
            raise ValueError("Registration failed. This course is already full.")
        self.reg_by_student.setdefault(student_id, set()).add(course_id)
        self.reg_by_course.setdefault(course_id, set()).add(student_id)

    def get_students_in_course(self, course_id: str):
        ids = self.reg_by_course.get(course_id, set())
        return [self.students[sid] for sid in ids if sid in self.students]

    def get_courses_for_student(self, student_id: str):
        ids = self.reg_by_student.get(student_id, set())
        return [self.courses[cid] for cid in ids if cid in self.courses]

    def available_slots(self, course_id: str):
        c = self.courses.get(course_id)
        if not c:
            return 0
        used = len(self.reg_by_course.get(course_id, set()))
        return c.capacity - used

    # Persistence: separate JSON files
    def save(self):
        students_path = os.path.join(self.data_dir, "students.json")
        courses_path = os.path.join(self.data_dir, "courses.json")
        regs_path = os.path.join(self.data_dir, "registrations.json")
        with open(students_path, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students.values()], f, indent=2)
        with open(courses_path, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.courses.values()], f, indent=2)
        with open(regs_path, "w", encoding="utf-8") as f:
            json.dump({k: list(v) for k, v in self.reg_by_student.items()}, f, indent=2)

    def load(self):
        students_path = os.path.join(self.data_dir, "students.json")
        courses_path = os.path.join(self.data_dir, "courses.json")
        regs_path = os.path.join(self.data_dir, "registrations.json")
        try:
            if os.path.exists(students_path):
                with open(students_path, "r", encoding="utf-8") as f:
                    arr = json.load(f)
                for sd in arr:
                    s = Student.from_dict(sd)
                    self.students[s.student_id] = s
                    self.reg_by_student.setdefault(s.student_id, set())
            if os.path.exists(courses_path):
                with open(courses_path, "r", encoding="utf-8") as f:
                    arr = json.load(f)
                for cd in arr:
                    c = Course.from_dict(cd)
                    self.courses[c.course_id] = c
                    self.reg_by_course.setdefault(c.course_id, set())
            if os.path.exists(regs_path):
                with open(regs_path, "r", encoding="utf-8") as f:
                    regs = json.load(f)
                for sid, clist in regs.items():
                    self.reg_by_student[sid] = set(clist)
                    for cid in clist:
                        self.reg_by_course.setdefault(cid, set()).add(sid)
        except Exception:
            # If loading fails, start empty but do not crash
            pass
