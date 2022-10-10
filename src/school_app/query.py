from tkinter import S
from .models import Student, db
from src.app import app
from sqlalchemy.exc import SQLAlchemyError
from src.common.rollback_handler import session_handler


@session_handler
def get_students() -> list:
    """This function gets all students from the data base

    Returns:
        list: list of students as result row.
    """
    return db.session.query(Student).all()

