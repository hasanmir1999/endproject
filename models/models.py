from database import Base
from sqlalchemy import Column , String

class Student(Base):
    __tablename__ = 'student'
    firstname = Column(String)
    lastname = Column(String)
    fathername = Column(String)
    birth = Column(String)
    ids = Column(String)#سریال شناسنامه
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(String)
    studentid = Column(String , primary_key=True)#شماره دانشجویی
    cphone = Column(String)
    hphone = Column(String)
    department = Column(String) #دانشکده
    major = Column(String)
    married = Column(String)
    idnumber = Column(String) #کد ملی
    scourseids = Column(String) #کد دروس اخذ شده
    tids = Column(String) #کد اساتید

class Teacher(Base):
    __tablename__ = 'teacher'
    firstname = Column(String)
    lastname = Column(String)
    idnumber = Column(String )#کد ملی استاد
    department = Column(String)
    major = Column(String)
    birth = Column(String)
    lid = Column(String , primary_key=True)#شماره استادی
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(String)
    cphone = Column(String)
    hphone = Column(String)
    lcourseid = Column(String)#کد دروس ارئه شده

class Course(Base):
    __tablename__ = 'course'
    cid = Column(String , primary_key=True)#کد درس
    cname = Column(String)
    department = Column(String)#دانشکده
    credit = Column(String)#تعداد واحد
