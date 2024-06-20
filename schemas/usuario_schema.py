from utils.ma import ma
from marshmallow import fields

class UsuarioSchema(ma.Schema):
    id_usuario = fields.Integer()
    
    nombre = fields.String()
    apellido = fields.String()
    email = fields.String()
    contrasena = fields.String()
    telefono = fields.String()
    direccion = fields.String()
    fecha_registro = fields.Date()
    rol = fields.String()
    ubigeo = fields.String()
    
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many = True)