from model.realizaciontest import RealizacionTest
from schemas.estudiante_schema import EstudianteSchema
from schemas.test_schema import TestSchema
from utils.ma import ma

class RealizacionTestSchema(ma.Schema):
    class Meta:
        model = RealizacionTest
        fields = ('id_realizaciontest', 'id_test', 'id_estudiante', 'fecha','puntaje','nivel','observaciones', 'test', 'estudiante')

    test = ma.Nested(TestSchema)
    estudiante = ma.Nested(EstudianteSchema)

realizacionTest_Schema = RealizacionTestSchema()
realizacionesTest_Schema = RealizacionTestSchema(many=True)
