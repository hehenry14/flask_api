from src.app import db


class Student(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'),
        nullable=False)


class Teacher(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   students = db.relationship('Student', backref='teacher', lazy=True)


# db.create_all()
