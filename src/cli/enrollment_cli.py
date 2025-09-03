from rich.console import Console
from rich.table import Table
from sqlalchemy.orm import Session
from src.services import enrollment_service, student_service, course_service
from rich.prompt import Prompt

console = Console()

def handle_enrollments(db: Session):
    while True:
        console.print("\n[bold cyan]Enrollment Management[/bold cyan]")
        console.print("1. Enroll Student in a Course")
        console.print("2. View Enrollments for a Student")
        console.print("3. View Enrollments for a Course")
        console.print("4. Back to Main Menu")
        choice = Prompt.ask("Please select an option", choices=["1", "2", "3", "4"], default="4")

        if choice == '1':
            enroll_student_in_course(db)
        elif choice == '2':
            view_student_enrollments(db)
        elif choice == '3':
            view_course_enrollments(db)
        elif choice == '4':
            break

def enroll_student_in_course(db: Session):
    console.print("\n[bold green]Enroll Student in a Course[/bold green]")
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))

    student = student_service.get_student(db, student_id)
    if not student:
        console.print(f"[bold red]Student with ID {student_id} not found.[/bold red]")
        return

    course = course_service.get_course(db, course_id)
    if not course:
        console.print(f"[bold red]Course with ID {course_id} not found.[/bold red]")
        return

    enrollment = enrollment_service.enroll_student(db, student_id, course_id)
    console.print(f"Student '{student.first_name}' enrolled in course '{course.name}' successfully!")

def view_student_enrollments(db: Session):
    console.print("\n[bold blue]View Enrollments for a Student[/bold blue]")
    student_id = int(input("Enter student ID: "))

    student = student_service.get_student(db, student_id)
    if not student:
        console.print(f"[bold red]Student with ID {student_id} not found.[/bold red]")
        return

    enrollments = enrollment_service.get_enrollments_for_student(db, student_id)
    
    table = Table(title=f"Enrollments for {student.first_name} {student.last_name}")
    table.add_column("Enrollment ID", style="cyan")
    table.add_column("Course Name", style="magenta")

    for enrollment in enrollments:
        table.add_row(str(enrollment.id), enrollment.course.name)
    
    console.print(table)

def view_course_enrollments(db: Session):
    console.print("\n[bold blue]View Enrollments for a Course[/bold blue]")
    course_id = int(input("Enter course ID: "))

    course = course_service.get_course(db, course_id)
    if not course:
        console.print(f"[bold red]Course with ID {course_id} not found.[/bold red]")
        return

    enrollments = enrollment_service.get_enrollments_for_course(db, course_id)
    
    table = Table(title=f"Enrollments for {course.name}")
    table.add_column("Enrollment ID", style="cyan")
    table.add_column("Student Name", style="magenta")

    for enrollment in enrollments:
        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
        table.add_row(str(enrollment.id), student_name)
    
    console.print(table)
