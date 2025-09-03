from rich.console import Console
from rich.table import Table
from sqlalchemy.orm import Session
from src.services import course_service, teacher_service
from src.cli.menu import display_crud_menu

console = Console()

def handle_courses(db: Session):
    while True:
        choice = display_crud_menu("Course")
        if choice == '1':
            add_course(db)
        elif choice == '2':
            view_courses(db)
        elif choice == '3':
            update_course(db)
        elif choice == '4':
            delete_course(db)
        elif choice == '5':
            break

def add_course(db: Session):
    console.print("[bold green]Add a new course[/bold green]")
    name = input("Enter course name: ")
    teacher_id = int(input("Enter teacher ID for this course: "))
    teacher = teacher_service.get_teacher(db, teacher_id)
    if not teacher:
        console.print(f"[bold red]Teacher with ID {teacher_id} not found.[/bold red]")
        return
    course = course_service.create_course(db, name, teacher_id)
    console.print(f"Course '{course.name}' added successfully!")

def view_courses(db: Session):
    courses = course_service.get_courses(db)
    table = Table(title="All Courses")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Teacher", style="green")

    for course in courses:
        teacher_name = f"{course.teacher.first_name} {course.teacher.last_name}" if course.teacher else "N/A"
        table.add_row(str(course.id), course.name, teacher_name)
    
    console.print(table)

def update_course(db: Session):
    console.print("[bold yellow]Update a course[/bold yellow]")
    course_id = int(input("Enter course ID to update: "))
    name = input("Enter new name: ")
    teacher_id = int(input("Enter new teacher ID: "))
    teacher = teacher_service.get_teacher(db, teacher_id)
    if not teacher:
        console.print(f"[bold red]Teacher with ID {teacher_id} not found.[/bold red]")
        return
    course = course_service.update_course(db, course_id, name, teacher_id)
    if course:
        console.print(f"Course {course_id} updated successfully!")
    else:
        console.print(f"[bold red]Course with ID {course_id} not found.[/bold red]")

def delete_course(db: Session):
    console.print("[bold red]Delete a course[/bold red]")
    course_id = int(input("Enter course ID to delete: "))
    course = course_service.delete_course(db, course_id)
    if course:
        console.print(f"Course {course_id} deleted successfully!")
    else:
        console.print(f"[bold red]Course with ID {course_id} not found.[/bold red]")
