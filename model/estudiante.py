from utils.db import db
from model.usuario import Usuario

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    
    id_estudiante = db.Column(db.String(8), primary_key = True)
    
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    
    escuela = db.Column(db.String(20))
    anio_ingreso = db.Column(db.String(4))
    ciclo = db.Column(db.Integer)
    fecha_nacimiento = db.Column(db.Date)
    
    usuario = db.relationship('Usuario', backref = 'estudiante')
    
    def __init__(self, id_estudiante, id_usuario, escuela, anio_ingreso,
                 ciclo, fecha_nacimiento):
        self.id_estudiante = id_estudiante
        self.id_usuario = id_usuario
        self.escuela = escuela
        self.anio_ingreso = anio_ingreso
        self.ciclo = ciclo
        self.fecha_nacimiento = fecha_nacimiento