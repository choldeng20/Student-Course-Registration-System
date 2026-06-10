# Student Course Registration System

## What the project does

A simple command-line Student Course Registration System that lets you add students and courses, register students to courses, view enrollments, and persist data to JSON files.

## How to run the project

Requirements: Python 3.8+ (no external packages required).

From the repository root run:

```
python3 smoke_test.py
```

Or run the interactive app:

```
python3 main.py
```

Data files used for tests are in the [data_test](data_test) folder. The interactive app uses the `data/` folder by default.

## Features implemented

- Add and list students
- Add and list courses
- Register students to courses with capacity checks
- Prevent duplicate registrations
- Persist and load data from JSON files
- Utilities to view students in a course and courses for a student

## Classes used

- `services.school_system.SchoolSystem` — main system logic and persistence
- `models.student.Student` — student model
- `models.course.Course` — course model
- `models.person.Person` — base class for people

## How I validated the project

- Ran `smoke_test.py` which exercises add, register, and save flows. Output files for the smoke test are in the `screenshots/` folder.

## Screenshots

Smoke test output and terminal captures (PNG):

![Smoke test output 1](screenshots/Screenshot%20from%202026-06-11%2002-02-28.png)

![Smoke test output 2](screenshots/Screenshot%20from%202026-06-11%2002-05-39.png)
## GitHub repository link

Add your repository URL here: https://github.com/your-username/your-repo

## Notes

If you want me to run additional tests or to include actual image screenshots (PNG), tell me and I will run the commands and add PNG files to the `screenshots/` directory.
# Student Course Registration System

Terminal-based Python app to manage students, courses, and registrations.

Quick start

1. Run smoke test:

```bash
python3 "smoke_test.py"
```

2. Run the interactive CLI:

```bash
python3 "main.py"
```

Data folder: `data/` contains `students.json`, `courses.json`, and `registrations.json` after saving.
