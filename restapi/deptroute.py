from orm.models import Department
from config import db,app
from flask import jsonify

@app.route("/departments",methods=['GET'])
def getDepartments():
    departments=Department.query.all()
    departments=[ x.serialize() for x in departments]
    return jsonify(departments)
