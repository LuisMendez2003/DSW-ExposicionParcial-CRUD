from utils.db import db


class Provincia(db.Model):
    __tablename__ = 'provincia'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))

    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'))

    departamento = db.relationship('Departamento', backref = 'provincia')
    
    def __init__(self, nombre, departamento_id):
        self.nombre = nombre
        self.departamento_id = departamento_id