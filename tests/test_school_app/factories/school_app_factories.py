import factory
from src.school_app.models import Students, db

class StudentsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Students
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'User %d' % n)
