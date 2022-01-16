import pandas as pd
from flask import Flask
from flask_sqlalchemy_core import SQLAlchemy
from flask_restless import APIManager



app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/storage.db'
db = SQLAlchemy(app)

MANAGER =APIManager(app, flask_sqlalchemy_db=db)



db.create_all()
