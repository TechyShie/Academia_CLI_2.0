from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"Teacher(id={self.id}, name='{self.first_name} {self.last_name}')"
