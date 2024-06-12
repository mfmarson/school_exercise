import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware 
from sqlmodel import Session, select, func
from db import get_session
from models.courses import Courses
from models.enrollments import Enrollments
from models.students import Students

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students")
def list_students(session: Session = Depends(get_session)):
    # with Session(engine) as session:
        statement = select(Students)
        results = session.exec(statement).all()
        return results

@app.get("/courses")
def list_courses(session: Session = Depends(get_session)):
    # with Session(engine) as session:
        statement = select(Courses)
        results = session.exec(statement).all()
        return results
        
@app.get("/enrollments")
def list_enrollments(session: Session = Depends(get_session)):
    statement = select(Courses.name.label('course_name'), 
                           func.array_agg(Students.name).label('students')
                    ).select_from (Enrollments).join(Students,Students.id == Enrollments.student_id).join(Courses, Courses.id == Enrollments.course_id).group_by(Courses.name)
    results = session.exec(statement).mappings().all()
    return results
   
 # SELECT students.name, courses.name FROM Enrollments
    # INNER JOIN students ON students.id = enrollments.student_id
    # INNER JOIN courses ON course.id = enrollments.course_id;
    
# @app.get("/")

if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)