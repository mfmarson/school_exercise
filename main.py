import uvicorn
from fastapi import FastAPI

from sqlmodel import Session, select
from db import engine 
from models.courses import Courses
from models.enrollments import Enrollments
from models.students import Students

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students")
def list_students():
    with Session(engine) as session:
        statement = select(Students)
        results = session.exec(statement).all()
    return results

@app.get("/courses")
def list_courses():
    with Session(engine) as session:
        statement = select(Courses)
        results = session.exec(statement).all()
        
@app.get("/enrollments")
def list_enrollments():
    with Session(engine) as session:
        statement = select(Enrollments)
        results = session.exec(statement).all()
    return results
   

# @app.get("/")

if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)