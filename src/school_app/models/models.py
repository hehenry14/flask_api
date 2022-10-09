from src.app import db


class Students(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))


# db.create_all()
