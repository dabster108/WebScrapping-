from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Dikshanta",
        "age": 23,
        "year": "Year 22"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"Name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Input id", gt=0, lt=9)):
    return students.get(student_id, {"error": "Student not found"})

@app.post("/create-student/{student_id}")
def create_student(student_id : int , student: Student):
    if student_id in students:
        return{"Error" : " Student data already exit"}
