from src.school_app.models import db, Students
from sqlalchemy.exc import SQLAlchemyError

def update_name(id: int, new_name: str):
    row = db.session.query(Students).one_or_none()
    if row:
        try:
            row.name = new_name
            db.session.add(row)
            db.session.commit()
            db.session.flush()
        except SQLAlchemyError:
            db.session.rollback()
        finally:
            db.session.close()

