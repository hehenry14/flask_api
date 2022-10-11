from sqlalchemy.exc import SQLAlchemyError
from src.app import db

def session_handler(func, *args, **kwargs):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError:
            db.session.rollback()
        # finally:
        #     db.session.close()
    return inner
