from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from . import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    enrollments = relationship("Enrollment", back_populates="student")

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Failed email validation")
        return email

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')"
