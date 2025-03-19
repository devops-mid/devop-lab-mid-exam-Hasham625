from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15))  # Optional field
    adress = db.Column(db.String(50))  # Optional field
    date_of_birth = db.Column(db.Date)  # New field

