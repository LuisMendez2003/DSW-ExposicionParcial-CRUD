from utils.db import db
from model.usuario import Usuario 

class Especialista(db.Model):
    __tablename__ = 'especialista'
    
    id_especialista = db.Column(db.String(8), primary_key = True)
    
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    
    cedula_profesional = db.Column(db.String(5))
    especialidad = db.Column(db.String(20))
    anios_experiencia = db.Column(db.Integer)
    fecha_ingreso = db.Column(db.Date)
    
    usuario = db.relationship('Usuario', backref = 'especialista')
    
    def __init__(self, id_especialista, id_usuario, cedula_profesional,
                 especialidad,anios_experiencia, fecha_ingreso):
        self.id_especialista = id_especialista
        self.id_usuario = id_usuario
        self.cedula_profesional = cedula_profesional
        self.especialidad = especialidad
        self.anios_experiencia = anios_experiencia
        self.fecha_ingreso = fecha_ingreso