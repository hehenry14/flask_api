import factory
from src.school_app.models import Student, Grade, db

class GradeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Grade
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Grade %d' % n)

    
class StudentsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Student
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'User %d' % n)

    grades = factory.List([
        factory.SubFactory(GradeFactory) for _ in range(5)
    ])
