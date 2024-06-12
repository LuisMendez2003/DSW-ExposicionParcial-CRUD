from model.alternativa import Alternativa
from schemas.pregunta_schema import PreguntaSchema
from utils.ma import ma
from marshmallow import fields

class AlternativaSchema(ma.Schema):
    class Meta:
        model = Alternativa
        fields = ('id_alternativa','id_pregunta','texto','puntaje','pregunta')

pregunta = ma.Nested(PreguntaSchema)

alternativa_schema = AlternativaSchema()
alternativas_schema = AlternativaSchema(many=True)
