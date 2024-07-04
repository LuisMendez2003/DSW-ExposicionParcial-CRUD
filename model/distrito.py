from utils.db import db

class Distrito(db.Model):

    __tablename__ = 'distrito'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    ubigeo = db.Column(db.String(6))


    provincia_id = db.Column(db.Integer, db.ForeignKey('provincia.id'))

    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)

    provincia = db.relationship('Provincia', backref = 'distrito')
    
    def __init__(self, nombre,ubigeo, provincia_id, latitud, longitud):
        self.nombre = nombre
        self.ubigeo = ubigeo
        self.provincia_id = provincia_id
        self.latitud = latitud
        self.longitud = longitud