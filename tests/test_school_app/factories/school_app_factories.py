import factory
from src.school_app.models import Student, Teacher, db

class StudentsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Student
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Student %d' % n)

class TeacherFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Teacher
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Teacher %d' % n)
    student = factory.SubFactory
    

