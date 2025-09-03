# Academia CLI: Course Registration System

## Problem Statement

This project is a command-line interface  application for managing a course registration system. It allows for the management of students, teachers, courses, and enrollments. The system is designed to be used by an academic administrator.

## Solution

The solution is a Python-based CLI application that uses SQLAlchemy for the Object-Relational Mapping , Alembic for database migrations, and Rich for an enhanced command-line experience. The application follows a clean architecture, separating models, services, and the CLI into different modules.

## Video Presentation

Add your video presentation link here:

- [Watch demo here](https://drive.google.com/file/d/1bCSBE95HdDk3dfNoSrR3Hjy27AA5pvG7/view?usp=sharing)

## Features

- **Student Management**: Add, view, update, and delete students.
- **Teacher Management**: Add, view, update, and delete teachers.
- **Course Management**: Add, view, update, and delete courses.
- **Enrollment Management**: Enroll students in courses and view enrollments.
- **Database Migrations**: Use Alembic to manage database schema changes.
- **Input Validation**: Validates user input, such as emails and positive integers.

## Project Structure

```
.
├── alembic/
│   ���── versions/
│   │   └── <initial_migration>.py
│   ├── env.py
│   └── script.py.mako
├── src/
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── course_cli.py
│   │   ├── enrollment_cli.py
│   │   ├── menu.py
│   │   ├── student_cli.py
│   │   └── teacher_cli.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── course.py
│   │   ├── enrollment.py
│   │   ├── student.py
│   │   └── teacher.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── course_service.py
│   │   ├── enrollment_service.py
│   │   ├── student_service.py
│   │   └── teacher_service.py
│   └── __init__.py
├── .gitignore
├── alembic.ini
├── main.py
├── Pipfile
└── README.md
```

## How to Install and Run

1.  **Clone the repository**:
    ```bash
    git clone git@github.com:TechyShie/Academia_CLI_2.0.git
    cd Academia_CLI_2.0
    ```

2.  **Install dependencies**:
    Make sure you have `pipenv` installed (`pip install pipenv`).
    ```bash
    pipenv install
    pipenv shell
    ```

3.  **Set up the database**:
    Run the Alembic migration to create the database tables.
    ```bash
    alembic upgrade head
    ```

4.  **Run the application**:
    ```bash
    python main.py
    ```

## Usage Examples

- **Add a student**:
  - Navigate to `Manage Students` -> `Add Student`.
  - Enter the first name, last name, and email.
- **Enroll a student in a course**:
  - Navigate to `Manage Enrollments` -> `Enroll Student in a Course`.
  - Enter the student ID and course ID.

## Relationships

- **Teacher-Course**: A teacher can have multiple courses (One-to-Many).
- **Student-Course**: A student can be enrolled in multiple courses, and a course can have multiple students (Many-to-Many, via the `enrollments` table).



## License

This project is licensed under the MIT License. 

## Author

- Susan Wanjiru
