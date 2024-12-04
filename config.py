from sqlalchemy import * 
from sqlalchemy.orm import Session

class DBSettings():
    @staticmethod
    def get_session():
        engine = create_engine(f"postgresql+psycopg2://postgres:root@localhost:5432/PythonDB")
        return Session(bind=engine)