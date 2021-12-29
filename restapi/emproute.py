from orm.models import Department,Employee
from config import db,app
from flask import jsonify,request,abort

@app.route("/employees",methods=['GET'])
def getEmployees():
    employees=Employee.query.all()
    employees=[ x.serialize() for x in employees]
    print(employees)
    return jsonify(employees)

