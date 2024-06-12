from utils.db import db
from model.test import Test

class Pregunta(db.Model):
    __tablename__ = 'pregunta'
    id_pregunta = db.Column(db.Integer, primary_key = True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    texto = db.Column(db.String(100))

    test = db.relationship('Test', backref = 'pregunta')

    def __init__(self,id_test,texto):
        self.id_test = id_test
        self.texto = texto