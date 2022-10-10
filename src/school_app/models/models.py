from bdb import GENERATOR_AND_COROUTINE_FLAGS
from src.app import db


class Student(db.Model):
   __tablename__ = 'student'
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   grades = db.relationship('Grade', lazy='subquery')

class Grade(db.Model):
   __tablename__ = 'grade'
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))

   student_id = db.Column(db.Integer, db.ForeignKey("student.id"))


# db.create_all()
