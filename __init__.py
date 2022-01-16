import pandas as pd
from flask import Flask
from flask_sqlalchemy_core import SQLAlchemy

app= Flask(__name__)

@app.route('/')
def index():
    return "hello word!"





app.run(host='0.0.0.0')
