from flask import Flask
from config import db
from orm.models import Department

class Employee(db.Model):
    __tablename__='employees'
    employee_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)
    basic=db.Column(db.Float,index=False,unique=False,nullable=False)
    desig=db.Column(db.String(30),index=False,unique=False,nullable=False)
    department_id = db.Column(db.Integer ,db.ForeignKey('departments.department_id'))
    department=db.relationship("Department",back_populates="employees")

    def __init__(self,name):
        self.name=name
    
    def serialize(self):
        return {
            'employee_id':self.employee_id,
            'name':self.name,
            'desig':self.desig,
            'basic':self.basic,
            'department':self.department.serialize()
            }
    
    def __repr__(self):
        return str(self.serialize())

Department.employees=db.relationship("Employee", back_populates="department")