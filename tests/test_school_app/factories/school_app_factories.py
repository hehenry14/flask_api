import factory
from src.school_app.models import Student, db

class StudentsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Student
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'User %d' % n)
