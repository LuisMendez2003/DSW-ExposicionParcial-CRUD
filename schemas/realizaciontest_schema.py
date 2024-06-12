from model.realizaciontest import RealizacionTest
from schemas.estudiante_schema import EstudianteSchema
from schemas.test_schema import TestSchema
from utils.ma import ma
from marshmallow import fields

class RealizacionTestSchema(ma.Schema):
    class Meta:
        model = RealizacionTest
        fields = ('id_realizaciontest','id_test','id_estudiante','fecha','test','estudiante')

        test = ma.Nested(TestSchema)
        estudiante = ma.Nested(EstudianteSchema)
    
realizacionTest_Schema = RealizacionTestSchema()
realizacionesTest_Schema = RealizacionTestSchema(many=True)