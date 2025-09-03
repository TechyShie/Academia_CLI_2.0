from sqlalchemy.orm import Session
from src.models.enrollment import Enrollment
from src.models.student import Student
from src.models.course import Course

def enroll_student(db: Session, student_id: int, course_id: int):
    db_enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def get_enrollments_for_student(db: Session, student_id: int):
    return db.query(Enrollment).filter(Enrollment.student_id == student_id).all()

def get_enrollments_for_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first().enrollments
