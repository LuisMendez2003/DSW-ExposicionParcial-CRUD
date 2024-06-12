from flask import Blueprint, jsonify, make_response
from utils.db import db
from model.test import Test
from model.pregunta import Pregunta
from model.alternativa import Alternativa
from schemas.pregunta_schema import pregunta_schema, preguntas_schema
from schemas.alternativa_schema import alternativa_schema, alternativas_schema

# Crear un nuevo Blueprint para el servicio combinado
preguntas_alternativas_services = Blueprint("preguntas_alternativas_services", __name__)

# Endpoint para obtener preguntas y alternativas de un test específico
@preguntas_alternativas_services.route('/test/<int:id_test>/preguntas-alternativas', methods=['GET'])
def get_preguntas_alternativas(id_test):
    test = Test.query.get(id_test)

    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    preguntas = Pregunta.query.filter_by(id_test=id_test).all()
    preguntas_result = preguntas_schema.dump(preguntas)

    preguntas_y_alternativas = []

    for pregunta in preguntas:
        alternativas = Alternativa.query.filter_by(id_pregunta=pregunta.id_pregunta).all()
        alternativas_result = alternativas_schema.dump(alternativas)
        preguntas_y_alternativas.append({
            'pregunta': pregunta_schema.dump(pregunta),
            'alternativas': alternativas_result
        })

    data = {
        'message': 'Preguntas y Alternativas del Test',
        'status': 200,
        'data': preguntas_y_alternativas
    }

    return make_response(jsonify(data), 200)
