from unittest import TestCase
from flask_sqlalchemy import SQLAlchemy
from .factories.school_app_factories import StudentsFactory
from src.school_app.models.models import db
from src.app import create_test_app, db
from flask import Flask
from src.school_app.query import get_students


class TestSchoolApp(TestCase):

    def create_app(self):
        return create_test_app()


    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_happy_flow(self):
        for i in range(5):
            StudentsFactory()
        result = get_students()
        self.assertAlmostEquals(len(result), 5)
