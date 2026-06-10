# Reflection

This project implements a simple Student Course Registration System as a CLI application. Building it reinforced core design patterns for small Python projects: separating models, services, and CLI logic; using JSON files for lightweight persistence; and validating business rules (e.g., course capacity and duplicate registrations).

What I learned:
- Designing small domain models (`Person`, `Student`, `Course`) makes the system easier to test and reason about.
- Keeping persistence separate (in `SchoolSystem`) simplifies swapping storage later.
- Writing a smoke test (`smoke_test.py`) is an efficient way to validate basic flows.

Next steps I would take if continuing:
- Add automated unit tests and CI configuration
- Add proper input validation and clearer error types
- Add a small web UI or REST API wrapper
