from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.respuesta import Respuesta
from schemas.realizaciontest_schema import RealizacionTestSchema
from schemas.respuesta_schema import respuesta_schema, respuestas_schema

respuesta_services = Blueprint("respuesta_services", __name__)

# Crear una Respuesta
@respuesta_services.route('/respuesta', methods=['POST'])
def create_respuesta():
    id_realizaciontest = request.json.get('id_realizaciontest')
    alternativa = request.json.get('alternativa')

    new_respuesta = Respuesta(id_realizaciontest=id_realizaciontest, alternativa=alternativa)

    db.session.add(new_respuesta)
    db.session.commit()

    result = respuesta_schema.dump(new_respuesta)

    data = {
        'message': 'Nueva Respuesta creada - Completado',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Obtener todas las Respuestas
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
