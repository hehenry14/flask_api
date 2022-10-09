from tkinter import S
from .models import Student, db
from src.app import app
from sqlalchemy.exc import SQLAlchemyError


def get_students() -> list:
    """This function gets all students from the data base

    Returns:
        list: list of students as result row.
    """
    try:
        return db.session.query(Student).all()
    except SQLAlchemyError:
        db.session.rollback()
    finally:
        db.session.close()

