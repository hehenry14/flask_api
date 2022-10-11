from unittest import TestCase
from .factories.school_app_factories import StudentsFactory, GradeFactory
from src.school_app.models.models import db, Student, Grade
from src.app import create_app, db
from sqlalchemy.exc import SQLAlchemyError

from src.school_app.query import get_students
from src.school_app.mutation import update_name, update_grade


class TestSchoolApp(TestCase):

    def create_app(self):
        return create_app("sqlite:///test.db")

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_student_model_relationship(self):
        student = StudentsFactory()
        grades = db.session.query(Grade).all()
        self.assertEqual(len(grades), 5)
        for grade in grades:
            self.assertEqual(grade.student_id, student.id)

    def test_student_model(self):
        for i in range(5):
            StudentsFactory()
        result = get_students()
        self.assertEquals(len(result), 5)
    
    def test_grade_model(self):
        for i in range(5):
            GradeFactory()
        grades = db.session.query(Grade).all()
        self.assertEquals(len(grades), 5)


    def test_update_name(self):
        student = StudentsFactory()
        update_name(student.id, 'test')
        expected_row = db.session.query(Student).filter(Student.name=='test').one_or_none()
        self.assertIsNotNone(expected_row)

    def test_relationships(self):
        student = StudentsFactory()
        grade = GradeFactory()
        update_grade(student.id, grade.id)
        test_student = db.session.query(Student).filter(Student.id == student.id).one()
        grades_ids = [stu_grade.id for stu_grade in test_student.grades]
        self.assertIn(grade.id, grades_ids)


