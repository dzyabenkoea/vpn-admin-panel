from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://user:pass@localhost:5488/db")

def connect():
    return Session(bind=engine)