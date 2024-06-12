from utils.db import db
from model.realizaciontest import RealizacionTest

class Respuesta(db.Model):
    __tablename__ = 'respuesta'
    id_respuesta = db.Column(db.Integer, primary_key = True)
    id_realizaciontest = db.Column(db.Integer, db.ForeignKey('realizacionTest.id_realizaciontest'))
    alternativa = db.Column(db.Integer)

    realizacionTest = db.relationship('RealizacionTest', backref = 'respuesta')

    def __init__(self,id_realizaciontest,alternativa):
        self.id_realizaciontest = id_realizaciontest
        self.alternativa = alternativa