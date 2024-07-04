from model.nivel import Nivel
from schemas.test_schema import TestSchema
from utils.ma import ma
from marshmallow import fields

class NivelSchema(ma.Schema):
    class Meta:
        model = Nivel
        fields = ('id_pregunta','id_test','texto','test')
        
    test = ma.Nested(TestSchema)
    
nivel_schema = NivelSchema()
niveles_schema = NivelSchema(many = True)