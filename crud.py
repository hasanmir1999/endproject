from schemas import schemas
from fastapi import HTTPException
from database import Session
from models import models

def addstudent(student:schemas.Student , db : Session):
    studentdb = models.Student( firstname = student.firstname ,
    lastname = student.lastname ,
    fathername = student.fathername ,
    birth = student.birth ,
    ids = student.ids ,#سریال شناسنامه
    borncity = student.borncity ,
    address = student.address ,
    studentid = student.studentid,#شماره دانشجویی
    postalcode = student.postalcode ,
    cphone = student.cphone ,
    hphone = student.hphone ,
    department = student.department , #دانشکده
    major = student.major ,
    married = student.married ,
    idnumber = student.idnumber , #کد ملی
    scourseids = student.scourseids , #کد دروس اخذ شده
    tids = student.tids #کد اساتید
    )
    db.add(studentdb)
    db.commit()
    return student

def readstudent(id: str , db : Session):
    student = db.query(models.Student).filter(models.Student.studentid == id).first()
    if not student : 
        raise HTTPException(status_code=404 , detail='دانشجویی با این شماره دانشجویی یافت نشد.')
    return student

def updatestudent(id: int, new_data: schemas.Student, db: Session):
    student_query = db.query(models.Student).filter(models.Student.studentid == id)

    if not student_query.first():
        raise HTTPException(status_code=404, detail="دانشجو یافت نشد")
    student_query.update(new_data.model_dump())
    db.commit()
    return new_data

def deletestudent(id: str , db : Session):
    student = db.query(models.Student).filter(models.Student.studentid == id).first()
    if not student:
        raise HTTPException(status_code=404 , detail='دانشجویی با شماره دانشجویی وارد شده وجود ندارد.')
    db.delete(student)
    db.commit()
    return student


#student

def addteacher(teacher:schemas.Teacher , db : Session):
    teacherdb = models.Teacher( firstname = teacher.firstname ,
    lastname = teacher.lastname ,
    birth = teacher.birth ,
    borncity = teacher.borncity ,
    address = teacher.address ,
    idnumber = teacher.idnumber,#کد ملی استاد
    postalcode = teacher.postalcode ,
    cphone = teacher.cphone ,
    hphone = teacher.hphone ,
    department = teacher.department , #دانشکده
    major = teacher.major ,
    lid = teacher.lid , # شماره استادی
    lcourseid = teacher.lcourseid , #کد دروس اخذ شده
    )
    db.add(teacherdb)
    db.commit()
    return teacher

def readteacher(id: str , db : Session):
    teacher = db.query(models.Teacher).filter(models.Teacher.lid == id).first()
    if not teacher : 
        raise HTTPException(status_code=404 , detail='استادی با این شماره استادی یافت نشد.')
    return teacher

def deleteteacher(id: str , db : Session):
    teacher = db.query(models.Teacher).filter(models.Teacher.lid == id).first()
    if not teacher:
        raise HTTPException(status_code=404 , detail='استادی با این شماره استادی وجود ندارد.')
    db.delete(teacher)
    db.commit()
    return teacher

def updateteacher(id: int, new_data: schemas.Teacher, db: Session):
    teacher_query = db.query(models.Teacher).filter(models.Teacher.lid == id)

    if not teacher_query.first():
        raise HTTPException(status_code=404, detail="استاد یافت نشد")
    teacher_query.update(new_data.model_dump())
    db.commit()
    return new_data


#teacher

def addcourse(course:schemas.Course , db : Session):
    coursedb = models.Course(
    courseid = course.cid ,
    coursename = course.cname,
    department = course.department,
    courseredit = course.credit
    )
    db.add(coursedb)
    db.commit()
    return course

def readcourse(id: str , db : Session):
    course = db.query(models.Course).filter(models.Course.cid == id).first()
    if not course : 
        raise HTTPException(status_code=404 , detail='درسی با این کد یافت نشد.')
    return course

def deletecourse(id: str , db : Session):
    course = db.query(models.Course).filter(models.Course.cid == id).first()
    if not course:
        raise HTTPException(status_code=404 , detail='درسی با این کد یافت نشد.')
    db.delete(course)
    db.commit()
    return course

def updatecourse(id: int, new_data: schemas.Course, db: Session):
    course_query = db.query(models.Course).filter(models.Course.cid == id)

    if not course_query.first():
        raise HTTPException(status_code=404, detail="درس یافت نشد")
    course_query.update(new_data.model_dump())
    db.commit()
    return new_data