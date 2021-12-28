from flask import Flask
from config import db

class Department(db.Model):
    __table__='departments'
    department_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)

    def __init__(self,name):
        self.name=name
    
    def serialize(self):
        return {'department_id':self.department_id,'name':self.name}
    
    def __repr__(self):
        return str(self.serialize())