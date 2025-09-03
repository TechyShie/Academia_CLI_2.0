from sqlalchemy.orm import Session
from src.models.student import Student

def create_student(db: Session, first_name: str, last_name: str, email: str):
    db_student = Student(first_name=first_name, last_name=last_name, email=email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, student_id: int, first_name: str, last_name: str, email: str):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.first_name = first_name
        db_student.last_name = last_name
        db_student.email = email
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student
