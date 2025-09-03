from rich.console import Console
from rich.table import Table
from sqlalchemy.orm import Session
from src.services import student_service
from src.cli.menu import display_crud_menu

console = Console()

def handle_students(db: Session):
    while True:
        choice = display_crud_menu("Student")
        if choice == '1':
            add_student(db)
        elif choice == '2':
            view_students(db)
        elif choice == '3':
            update_student(db)
        elif choice == '4':
            delete_student(db)
        elif choice == '5':
            break

def add_student(db: Session):
    console.print("[bold green]Add a new student[/bold green]")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    try:
        student = student_service.create_student(db, first_name, last_name, email)
        console.print(f"Student '{student.first_name} {student.last_name}' added successfully!")
    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

def view_students(db: Session):
    students = student_service.get_students(db)
    table = Table(title="All Students")
    table.add_column("ID", style="cyan")
    table.add_column("First Name", style="magenta")
    table.add_column("Last Name", style="magenta")
    table.add_column("Email", style="green")

    for student in students:
        table.add_row(str(student.id), student.first_name, student.last_name, student.email)

    console.print(table)

def update_student(db: Session):
    console.print("[bold yellow]Update a student[/bold yellow]")
    student_id = int(input("Enter student ID to update: "))
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    email = input("Enter new email: ")
    try:
        student = student_service.update_student(db, student_id, first_name, last_name, email)
        if student:
            console.print(f"Student {student_id} updated successfully!")
        else:
            console.print(f"[bold red]Student with ID {student_id} not found.[/bold red]")
    except ValueError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

def delete_student(db: Session):
    console.print("[bold red]Delete a student[/bold red]")
    student_id = int(input("Enter student ID to delete: "))
    student = student_service.delete_student(db, student_id)
    if student:
        console.print(f"Student {student_id} deleted successfully!")
    else:
        console.print(f"[bold red]Student with ID {student_id} not found.[/bold red]")
