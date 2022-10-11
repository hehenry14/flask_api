from src.school_app.models import db, Student, Grade
from sqlalchemy.exc import SQLAlchemyError
from src.common.rollback_handler import session_handler


@session_handler
def update_name(student_id: int, new_name: str):
    row = db.session.query(Student).filter(Student.id == student_id).one_or_none()
    row.name = new_name
    db.session.add(row)
    db.session.commit()
    db.session.flush()


@session_handler
def update_grade(student_id: int, grade_id: int):
    row = db.session.query(Grade).filter(Grade.id == grade_id).one_or_none()
    row.student_id = student_id
    db.session.add(row)
    db.session.commit()
    db.session.flush()
