from sqlalchemy import true
from model.respuesta import Respuesta
from schemas.alternativa_schema import AlternativaSchema
from schemas.realizaciontest_schema import RealizacionTestSchema
from utils.ma import ma
from marshmallow import fields

class RespuestaSchema(ma.Schema):
    class Meta:
        model = Respuesta
        fields = ('id_respuesta','id_realizaciontest','alternativa','realizacionTest','alternativa_relacionada')

    realizacionTest = ma.Nested(RealizacionTestSchema)
    alternativa_relacionada = ma.Nested(AlternativaSchema)

respuesta_schema = RespuestaSchema()
respuestas_schema = RespuestaSchema(many=true)


