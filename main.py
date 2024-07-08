from fastapi import FastAPI, Depends
from schemas.schemas import Student , Teacher , Course
import crud
from models import models
from database import Session , get_db , engine
app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/addStu' , response_model = Student)
def addStudent(student:Student , db: Session = Depends(get_db)):
    return crud.addstudent(student, db)

@app.get('/readStu{studentid}')
def readStudent(studentid : str , db:Session = Depends(get_db)):
    return crud.readstudent(studentid , db)

@app.delete('/delStu{studentid}')
def deleteStudent(studentid : str , db:Session = Depends(get_db)):
    return crud.deletestudent(studentid, db)

@app.patch("/updateStu{id}")
def updateStudent(id: int, new_data: Student, db: Session = Depends(get_db)):
    return crud.updatestudent(id= id, new_data = new_data, db= db)

#student


@app.post('/addTeach' , response_model = Teacher)
def addTeacher(teacher:Teacher , db: Session = Depends(get_db)):
    return crud.addTeacher(teacher, db)

@app.get('/readTeach{teacherid}')
def readTeacher(teacherid : str , db:Session = Depends(get_db)):
    return crud.readteacher(teacherid , db)



@app.delete('/delTeach{teacherid}')
def deleteTeacher(teacherid : str , db:Session = Depends(get_db)):
    return crud.deleteTeacher(teacherid, db)

@app.patch("/updateTeach{id}")
def updateTeacher(id: int, new_data: Teacher, db: Session = Depends(get_db)):
    return crud.updateteacher(id= id, new_data = new_data, db= db)

#teacher

@app.post('/addcou' , response_model = Course)
def addCourse(course:Course , db: Session = Depends(get_db)):
    return crud.addCourse(course, db)

@app.get('/readcou{courseid}')
def readCourse(courseid : str , db:Session = Depends(get_db)):
    return crud.readteacher(courseid , db)

@app.delete('/delcou{courseid}')
def deleteCourse(courseid : str , db:Session = Depends(get_db)):
    return crud.deleteCourse(courseid, db)

@app.patch("/updatecou{id}")
def updateCourse(id: int, new_data: Course, db: Session = Depends(get_db)):
    return crud.updatecourse(id= id, new_data = new_data, db= db)