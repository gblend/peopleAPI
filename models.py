from datetime import datetime
from config import db, ma


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)
    timestamp = db.Column(db.DateTime,
                          default=datetime.utcnow,
                          onupdate=datetime.utcnow)
    
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email


class PersonSchema(ma.Schema):
    class Meta:
        fields = ('fname', 'lname', 'email', 'timestamp')
        model = Person
        
