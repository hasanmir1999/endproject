from sqlalchemy.orm import sessionmaker , Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

URL = 'sqlite:///./sql_app.db'

engine = create_engine(URL , connect_args={"check_same_thread": False})

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try: 
        yield db
    finally: 
        db.close()