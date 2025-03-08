from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# app = FastAPI()

# students = {
#     1: {
#         "name": "Dikshanta",
#         "age": 23,
#         "year": "Year 22"
#     }
# }


# class Student(BaseModel):
#     name: str
#     age: int
#     year: str


# class UpdateStudent(BaseModel):
#     name: Optional[str] = None
#     age: Optional[int] = None
#     year: Optional[str] = None


# @app.get("/")
# def index():
#     return {"Name": "First Data"}


# @app.get("/get-student/{student_id}")
# def get_student(student_id: int = Path(..., description="Input id", gt=0, lt=9)):
#     return students.get(student_id, {"error": "Student not found"})

# @app.post("/create-student/{student_id}")
# def create_student(student_id : int , student: Student):
#     if student_id in students:
#         return{"Error" : " Student data already exit"}


app = FastAPI()
# @app.get("/")
# def home():
#     return{"Data": "Test"}

# @app.get("/about")
# def about():
#     return{"Data" : " About"}


inventory = {
    1: {
        "name" : "Laptop",
        "price" : 5000,
        "brand" : "Acer"

    }

}

# path - to give detailing 
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="The ID of the item" , gt = 0 , lt = 4)):
    return inventory[item_id]



@app.get("/get-name")
def get_item(name : str):
    for item_id in inventory:
        if inventory[item_id] [name] == " name":
            return inventory[item_id]
    return {"Data" : "Not found"}

