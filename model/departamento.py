from utils.db import db

class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    
    def __init__(self, nombre):
        self.nombre = nombre