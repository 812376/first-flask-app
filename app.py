
from flask.app import Flask

from flask import Flask

app=Flask(__name__)

@app.route("/")
def greet():
    return "Flask App is running..!!!"