from utils.ma import ma
from model.especialista import Especialista
from marshmallow import fields
from schemas.usuario_schema import UsuarioSchema

class EspecialistaSchema(ma.Schema):
    class Meta:
        model = Especialista
        fields = ('id_especialista','id_usuario','cedula_profesional',
                  'especialidad','anios_experiencia','fecha_ingreso','usuario')
        
    usuario = ma.Nested(UsuarioSchema)

especialista_schema = EspecialistaSchema()
especialistas_schema = EspecialistaSchema(many = True)    