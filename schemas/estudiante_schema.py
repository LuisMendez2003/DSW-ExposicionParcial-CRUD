from utils.ma import ma
from model.estudiante import Estudiante
from marshmallow import fields
from schemas.usuario_schema import UsuarioSchema

class EstudianteSchema(ma.Schema):
    class Meta:
        model = Estudiante        
        fields = ('id_estudiante','id_usuario','escuela','anio_ingreso',
                  'ciclo','fecha_nacimiento','usuario')
        
    usuario = ma.Nested(UsuarioSchema)
    
estudiante_schema = EstudianteSchema()
estudiantes_schema = EstudianteSchema(many = True)
        