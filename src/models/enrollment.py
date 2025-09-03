from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"Enrollment(id={self.id}, student_id={self.student_id}, course_id={self.course_id})"
