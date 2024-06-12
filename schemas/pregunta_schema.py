from model.pregunta import Pregunta
from schemas.test_schema import TestSchema
from utils.ma import ma
from marshmallow import fields

class PreguntaSchema(ma.Schema):
    class Meta:
        model = Pregunta
        fields = ('id_pregunta','id_test','texto','test')
        
    test = ma.Nested(TestSchema)
    
pregunta_schema = PreguntaSchema()
preguntas_schema = PreguntaSchema(many = True)