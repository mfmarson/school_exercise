from.base import Base

class Enrollments(Base, table=True):
    __tablename__ = "enrollments"
    
    student_id: int
    course_id: int
    enrollment_date: int
    
 
    def __repr__(self):
        return f"<Enrollments{self.name!r}>"