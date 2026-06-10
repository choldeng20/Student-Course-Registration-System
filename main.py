from services.school_system import SchoolSystem


def prompt(text):
    return input(text).strip()


def main():
    system = SchoolSystem(data_dir="data")
    system.load()

    MENU = """
===== Student Course Registration System =====

1. Add Student
2. View Students
3. Search Student
4. Add Course
5. View Courses
6. Register Student to Course
7. View Students in a Course
8. View Courses for a Student
9. Save Data
10. Load Data
0. Exit

Choose an option: """

    while True:
        try:
            choice = prompt(MENU)
            if choice == "1":
                sid = prompt("Student ID: ")
                name = prompt("Name: ")
                email = prompt("Email: ")
                phone = prompt("Phone: ")
                try:
                    s = system.add_student(sid, name, email, phone)
                    print(f"Added {s.student_id} - {s.name}")
                except Exception as e:
                    print("Error:", e)
            elif choice == "2":
                for s in system.get_all_students():
                    print(s.display())
                    print("---")
            elif choice == "3":
                q = prompt("Enter student ID or name to search: ")
                results = system.search_students(q)
                if not results:
                    print("No students found")
                for s in results:
                    print(s.display())
                    print("---")
            elif choice == "4":
                cid = prompt("Course ID: ")
                name = prompt("Course Name: ")
                trainer = prompt("Trainer: ")
                capacity = prompt("Capacity: ")
                try:
                    c = system.add_course(cid, name, trainer, capacity)
                    print(f"Added {c.course_id} - {c.name}")
                except Exception as e:
                    print("Error:", e)
            elif choice == "5":
                for c in system.get_all_courses():
                    print(c.display())
                    print(f"Available slots: {system.available_slots(c.course_id)}")
                    print("---")
            elif choice == "6":
                sid = prompt("Student ID: ")
                cid = prompt("Course ID: ")
                try:
                    system.register_student_to_course(sid, cid)
                    s = system.find_student_by_id(sid)
                    c = system.find_course_by_id(cid)
                    print(f"{s.name} successfully registered for {c.name}.")
                except Exception as e:
                    print("Error:", e)
            elif choice == "7":
                cid = prompt("Course ID: ")
                students = system.get_students_in_course(cid)
                if not students:
                    print("No students registered or invalid course")
                for s in students:
                    print(s.display())
                    print("---")
            elif choice == "8":
                sid = prompt("Student ID: ")
                courses = system.get_courses_for_student(sid)
                if not courses:
                    print("No courses or invalid student")
                for c in courses:
                    print(c.display())
                    print("---")
            elif choice == "9":
                system.save()
                print("Data saved")
            elif choice == "10":
                system.load()
                print("Data loaded")
            elif choice == "0":
                system.save()
                print("Saved. Exiting.")
                break
            else:
                print("Invalid choice")
        except KeyboardInterrupt:
            print("\nInterrupted. Saving and exiting.")
            system.save()
            break


if __name__ == "__main__":
    main()
