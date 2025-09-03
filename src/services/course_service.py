from sqlalchemy.orm import Session
from src.models.course import Course

def create_course(db: Session, name: str, teacher_id: int):
    db_course = Course(name=name, teacher_id=teacher_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session):
    return db.query(Course).all()

def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db: Session, course_id: int, name: str, teacher_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db_course.name = name
        db_course.teacher_id = teacher_id
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course
