
from model.departamento import Departamento
from schemas.departamento_schema import DepartamentoSchema
from utils.ma import ma
from marshmallow import fields

class ProvinciaSchema(ma.Schema):
    class Meta:
        model = Departamento
        fields = ('id','nombre','departamento_id','departamento')
        
    departamento = ma.Nested(DepartamentoSchema)
    
provincia_schema = ProvinciaSchema()
provincias_schema = ProvinciaSchema(many = True)