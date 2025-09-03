from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def display_main_menu():
    console.print(Panel(
        "[bold cyan]Welcome to Academia CLI[/bold cyan]\n\n" \
        "1. Manage Students\n" \
        "2. Manage Teachers\n" \
        "3. Manage Courses\n" \
        "4. Manage Enrollments\n" \
        "5. Exit",
        title="Main Menu",
        expand=False
    ))
    choice = Prompt.ask("Please select an option", choices=["1", "2", "3", "4", "5"], default="5")
    return choice

def display_crud_menu(item_name: str):
    console.print(Panel(
        f"[bold cyan]Manage {item_name}[/bold cyan]\n\n" \
        f"1. Add {item_name}\n" \
        f"2. View all {item_name}s\n" \
        f"3. Update {item_name}\n" \
        f"4. Delete {item_name}\n" \
        f"5. Back to Main Menu",
        title=f"{item_name} Management",
        expand=False
    ))
    choice = Prompt.ask("Please select an option", choices=["1", "2", "3", "4", "5"], default="5")
    return choice
