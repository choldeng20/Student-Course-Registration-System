from services.school_system import SchoolSystem


def run():
    s = SchoolSystem(data_dir="data_test")
    # add students
    s.add_student("S001", "Alice", "alice@example.com", "0710000000")
    s.add_student("S002", "Bob", "bob@example.com", "0710000001")
    # add courses
    s.add_course("PY101", "Python Fundamentals", "Mr. Joseph", 2)
    s.add_course("HS201", "World History", "Mrs. Ann", 3)
    # register
    s.register_student_to_course("S001", "PY101")
    s.register_student_to_course("S002", "PY101")
    try:
        s.register_student_to_course("S001", "PY101")
    except Exception as e:
        print("Expected error on double registration:", e)
    print("Students in PY101:")
    for st in s.get_students_in_course("PY101"):
        print(st.display())
    print("Courses for S001:")
    for c in s.get_courses_for_student("S001"):
        print(c.display())
    s.save()
    print("Saved data to data_test/")


if __name__ == "__main__":
    run()
