from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

USER_DB = os.getenv("DB_USER")
PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("MYSQL_DATABASE")

URL_DATABASE = f"mysql+pymysql://{USER_DB}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
