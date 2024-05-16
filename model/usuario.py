from utils.db import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id_usuario = db.Column(db.Integer, primary_key = True)
    
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    email = db.Column(db.String(50))
    contrasena = db.Column(db.String(20))
    telefono = db.Column(db.String(9))
    direccion = db.Column(db.String(255))
    fecha_registro = db.Column(db.Date)
    rol = db.Column(db.String(20))
    
    def __init__(self, nombre, apellido, email, contrasena,
                 telefono, direccion, fecha_registro, rol):
        
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = fecha_registro
        self.rol = rol
