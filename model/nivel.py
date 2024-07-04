# models/nivel.py
from utils.db import db

class Nivel(db.Model):
    __tablename__ = 'nivel'
    id_nivel = db.Column(db.Integer, primary_key=True)
    id_test = db.Column(db.Integer, db.ForeignKey('test.id_test'))
    min_puntaje = db.Column(db.Integer)
    max_puntaje = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))

    test = db.relationship('Test', backref = 'nivel')

    def __init__(self, id_test, min_puntaje, max_puntaje, descripcion):
        self.id_test = id_test
        self.min_puntaje = min_puntaje
        self.max_puntaje = max_puntaje
        self.descripcion = descripcion