from sqlalchemy.orm import Session
from src.models.teacher import Teacher

def create_teacher(db: Session, first_name: str, last_name: str):
    db_teacher = Teacher(first_name=first_name, last_name=last_name)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teachers(db: Session):
    return db.query(Teacher).all()

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, first_name: str, last_name: str):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher:
        db_teacher.first_name = first_name
        db_teacher.last_name = last_name
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return db_teacher
