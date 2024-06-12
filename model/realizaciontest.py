from utils.db import db
from model.test import Test
from model.estudiante import Estudiante

class RealizacionTest(db.Model):
    __tablename__ = 'realizacionTest'
    id_realizaciontest = db.Column(db.Integer, primary_key = True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    id_estudiante = db.Column(db.String(8), db.ForeignKey('estudiante.id_estudiante'))
    fecha = db.Column(db.Date)

    test = db.relationship('Test', backref = 'realizacionTest')
    estudiante = db.relationship('Estudiante', backref = 'realizacionTest')

    def __init__(self,id_test,id_estudiante,fecha):
        self.id_test = id_test
        self.id_estudiante = id_estudiante
        self.fecha = fecha