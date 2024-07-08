from pydantic import BaseModel , Field , field_validator
from . import dependencies

from fastapi import HTTPException


class UserBase(BaseModel):
    firstname : str = Field(pattern= r'[آ-ی]{3,10}')
    lastname : str = Field(pattern= r'[آ-ی]{3,10}')
    birth : str = Field(pattern= r'@"^$|^([1۱][۰-۹ 0-9]{3}[/\/]([0 ۰][۱-۶ 1-6])[/\/]([0 ۰][۱-۹ 1-9]|[۱۲12][۰-۹ 0-9]|[3۳][01۰۱])|[1۱][۰-۹ 0-9]{3}[/\/]([۰0][۷-۹ 7-9]|[1۱][۰۱۲012])[/\/]([۰0][1-9 ۱-۹]|[12۱۲][0-9 ۰-۹]|(30|۳۰)))$')
    address : str = Field(pattern= r'\w{3,100}')
    idnumber : str = Field(pattern= r'\d{10}')
    borncity : str
    cphone : str = Field(pattern= r'(\+?989|0?9)\d{9}')
    hphone : str = Field(pattern= r'^0[0-9]{2,}[0-9]{7,}$')
    postalcode : str = Field(pattern= r'\d{10}')
    major : str 
    department : str 

    @field_validator('borncity')
    def validBornCity(cls, vbc):
        if not vbc in dependencies.IRAN_PROVINCE_CAPITALS:
            raise HTTPException(status_code=400 , detail='نام استان محل تولد باید با حروف فارسی و نام یکی از مراکز استان ایران باشد.')
        return vbc
    
    @field_validator('major')
    def validMajor(cls , vm):
        if not vm in dependencies.VALID_ENGI_DEPARTMENT_MAJORS:
            raise HTTPException(status_code=400 , detail='رشته ی تحصیلی باید با حروف فارسی و نام یکی از رشته های فنی مهندسی باشد.')
        return vm
    @field_validator('department')
    def validDepartment(cls , vd):
        if not vd in dependencies.VALID_DEPARTMENTS:
            raise HTTPException(status_code=400 , detail='نام دانشکده باید با حروف فارسی و نام یکی از دانشکده های دانشگاه لرستان باشد.')
        return vd

class Student(UserBase):
    studentid : str = Field(pattern=r'^40[12]114150\d[1-9]$')
    fathername : str = Field(pattern= r'[آ-ی]{3,10}')
    ids : str = Field(pattern=r'^\d{2}[آ-ی]\/\d{6}$')
    married : str = Field(pattern=r'^(مجرد|متاهل)$')
    scourseids : str
    tids : str

class Course(BaseModel):
    cid : str = Field(pattern= r'^\d{5}$')
    cname : str = Field(pattern= r'^[آ-ی]{3,25}$')
    department : str 
    credit : str = Field(pattern=r'^[1-4]$')
    @field_validator('department')
    def validDepartment(cls , vd):
        if not vd in dependencies.VALID_DEPARTMENTS:
            raise HTTPException(status_code=400 , detail='نام دانشکده باید با حروف فارسی و نام یکی از دانشکده های دانشگاه لرستان باشد.')
        return vd


class Teacher(UserBase):
    lid : str
    lcourseid: str

class Studentid(BaseModel):
    studentId : str = Field(pattern=r'^40[12]114150\d[1-9]$')

class Teacherid(BaseModel):
    Teacherid : str