from model.distrito import Distrito
from schemas.provincia_schema import ProvinciaSchema
from utils.ma import ma
from marshmallow import fields

class DistritoSchema(ma.Schema):
    class Meta:
        model = Distrito
        fields = ('id','nombre','ubigeo','provincia_id','latitud','longitud','provincia')
    
    provincia = ma.Nested(ProvinciaSchema)

distrito_schema = DistritoSchema()
distritos_schema = DistritoSchema(many = True)