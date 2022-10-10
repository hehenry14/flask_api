from src.school_app.models import db, Student
from sqlalchemy.exc import SQLAlchemyError
from src.common.rollback_handler import session_handler


@session_handler
def update_name(student_id: int, new_name: str):
    row = db.session.query(Student).filter(Student.id == student_id).one_or_none()
    row.name = new_name
    db.session.add(row)
    db.session.commit()
    db.session.flush()
