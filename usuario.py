from __init__ import db
from __init__ import manager


class Filme(db.Model):
    id= db.Column(db.Integer, primery_key=True)
    nome = db.Column(db.String(100))
    Data_Lançamento = db.Column(db.DateTime)
    Avalicao = db.Column(db.String(10))

    email = db.Column(db.String(20), unique=True)

db.create_all()
manager.create_api(Filme,methods=['POST','GET','PUT','DELETE'])
