from rich.console import Console
from rich.table import Table
from sqlalchemy.orm import Session
from src.services import teacher_service
from src.cli.menu import display_crud_menu

console = Console()

def handle_teachers(db: Session):
    while True:
        choice = display_crud_menu("Teacher")
        if choice == '1':
            add_teacher(db)
        elif choice == '2':
            view_teachers(db)
        elif choice == '3':
            update_teacher(db)
        elif choice == '4':
            delete_teacher(db)
        elif choice == '5':
            break

def add_teacher(db: Session):
    console.print("[bold green]Add a new teacher[/bold green]")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    teacher = teacher_service.create_teacher(db, first_name, last_name)
    console.print(f"Teacher '{teacher.first_name} {teacher.last_name}' added successfully!")

def view_teachers(db: Session):
    teachers = teacher_service.get_teachers(db)
    table = Table(title="All Teachers")
    table.add_column("ID", style="cyan")
    table.add_column("First Name", style="magenta")
    table.add_column("Last Name", style="magenta")

    for teacher in teachers:
        table.add_row(str(teacher.id), teacher.first_name, teacher.last_name)
    
    console.print(table)

def update_teacher(db: Session):
    console.print("[bold yellow]Update a teacher[/bold yellow]")
    teacher_id = int(input("Enter teacher ID to update: "))
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    teacher = teacher_service.update_teacher(db, teacher_id, first_name, last_name)
    if teacher:
        console.print(f"Teacher {teacher_id} updated successfully!")
    else:
        console.print(f"[bold red]Teacher with ID {teacher_id} not found.[/bold red]")

def delete_teacher(db: Session):
    console.print("[bold red]Delete a teacher[/bold red]")
    teacher_id = int(input("Enter teacher ID to delete: "))
    teacher = teacher_service.delete_teacher(db, teacher_id)
    if teacher:
        console.print(f"Teacher {teacher_id} deleted successfully!")
    else:
        console.print(f"[bold red]Teacher with ID {teacher_id} not found.[/bold red]")
