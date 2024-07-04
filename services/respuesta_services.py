from flask import Blueprint, request, jsonify, make_response
from model.alternativa import Alternativa
from model.nivel import Nivel
from model.realizaciontest import RealizacionTest
from utils.db import db
from model.respuesta import Respuesta
from schemas.realizaciontest_schema import RealizacionTestSchema
from schemas.respuesta_schema import respuesta_schema, respuestas_schema

respuesta_services = Blueprint("respuesta_services", __name__)

# Crear una Respuesta
@respuesta_services.route('/respuesta', methods=['POST','OPTIONS'])
def create_respuesta():

     #VERIFICA POST
    if request.method == 'OPTIONS':
        return make_response(jsonify({'message': 'Allow CORS', 'status': 200}), 200)

    id_realizaciontest = request.json.get('id_realizaciontest')
    alternativa = request.json.get('alternativa')

    new_respuesta = Respuesta(id_realizaciontest=id_realizaciontest, alternativa=alternativa)

    db.session.add(new_respuesta)

    # Guardar los cambios en la base de datos
    db.session.commit()

    result = respuesta_schema.dump(new_respuesta)

    data = {
        'message': 'Nueva Respuesta creada - Completado',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

#Actualizar puntaje
@respuesta_services.route('/actualizar_puntaje', methods=['POST'])
def actualizar_puntaje():
    id_realizaciontest = request.json.get('id_realizaciontest')

    # Obtener todas las respuestas para la realizacion de test
    respuestas = Respuesta.query.filter_by(id_realizaciontest=id_realizaciontest).all()

    # Calcular el puntaje total sumando los puntajes de las alternativas
    puntaje_total = sum(r.alternativa_relacionada.puntaje for r in respuestas if r.alternativa_relacionada)

    # Obtener la realizacion de test y actualizar su puntaje
    realizacion_test = RealizacionTest.query.get(id_realizaciontest)
    if not realizacion_test:
        return make_response(jsonify({'message': 'Realización de test no encontrada', 'status': 404}), 404)

    realizacion_test.puntaje = puntaje_total

    nivel = Nivel.query.filter(
        Nivel.id_test == realizacion_test.id_test,
        Nivel.min_puntaje <= puntaje_total,
        Nivel.max_puntaje >= puntaje_total
    ).first()

    if nivel:
        realizacion_test.nivel = nivel.descripcion
    else:
        realizacion_test.nivel = 'Indeterminado'

    db.session.commit()

    data = {
        'message': 'Puntaje actualizado - Completado',
        'puntaje': realizacion_test.puntaje,
        'status': 200
    }

    return make_response(jsonify(data), 200)

#Obtener todas las Respuestas
@respuesta_services.route('/respuestas', methods=['GET'])
def get_respuestas():
    all_respuestas = Respuesta.query.all()
    result = respuestas_schema.dump(all_respuestas)

    data = {
        'message': 'Todas las Respuestas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una Respuesta por ID
@respuesta_services.route('/respuesta/<int:id>', methods=['GET'])
def get_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = respuesta_schema.dump(respuesta)

    data = {
        'message': 'Respuesta encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Modificar una Respuesta
@respuesta_services.route('/respuesta/update/<int:id>', methods=['PUT'])
def update_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_realizaciontest = request.json.get('id_realizaciontest')
    alternativa = request.json.get('alternativa')

    respuesta.id_realizaciontest = id_realizaciontest
    respuesta.alternativa = alternativa

    db.session.commit()

    result = respuesta_schema.dump(respuesta)

    data = {
        'message': 'Respuesta actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Borrar una Respuesta
@respuesta_services.route('/respuesta/delete/<int:id>', methods=['DELETE'])
def delete_respuesta(id):
    respuesta = Respuesta.query.get(id)

    if not respuesta:
        data = {
            'message': 'Respuesta no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(respuesta)
    db.session.commit()

    data = {
        'message': 'Respuesta eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)
