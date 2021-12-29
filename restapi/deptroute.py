from orm.models import Department
from config import db,app
from flask import jsonify,request,abort

@app.route("/departments",methods=['GET'])
def getDepartments():
    departments=Department.query.all()
    departments=[ x.serialize() for x in departments]
    print(departments)
    return jsonify(departments)

@app.route("/departments",methods=['POST'])
def processDepartments():
    try:
        data=request.get_json()
        print(data)
        department=Department(data['name'])
        db.session.add(department)
        db.session.commit()
        return {"status": "success"}, 201
    except:
        abort({'status':"Internal server error"},500)