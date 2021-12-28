from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app=Flask(__name__,static_url_path="")

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("MYSQL_URL_PATTERN")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)