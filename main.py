from src.database.connection import SessionLocal, engine
from src.models import Base
from src.cli.menu import display_main_menu
from src.cli.student_cli import handle_students
from src.cli.teacher_cli import handle_teachers
from src.cli.course_cli import handle_courses
from src.cli.enrollment_cli import handle_enrollments

def main():
    # This is a good place to create tables if they don't exist
    # For a production app, you'd use Alembic migrations
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    while True:
        choice = display_main_menu()
        if choice == '1':
            handle_students(db)
        elif choice == '2':
            handle_teachers(db)
        elif choice == '3':
            handle_courses(db)
        elif choice == '4':
            handle_enrollments(db)
        elif choice == '5':
            break
    
    db.close()

if __name__ == "__main__":
    main()
