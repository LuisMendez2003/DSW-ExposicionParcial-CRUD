from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.alternativa import Alternativa
from schemas.pregunta_schema import PreguntaSchema
from schemas.alternativa_schema import alternativa_schema, alternativas_schema

alternativa_services = Blueprint("alternativa_services", __name__)

# Crear una Alternativa
@alternativa_services.route('/alternativa', methods=['POST'])
def create_alternativa():
    id_pregunta = request.json.get('id_pregunta')
    texto = request.json.get('texto')
    puntaje = request.json.get('puntaje')

    new_alternativa = Alternativa(id_pregunta=id_pregunta, texto=texto, puntaje=puntaje)

    db.session.add(new_alternativa)
    db.session.commit()

    result = alternativa_schema.dump(new_alternativa)

    data = {
        'message': 'Nueva Alternativa creada - Completado',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Obtener todas las Alternativas
@alternativa_services.route('/alternativas', methods=['GET'])
def get_alternativas():
    all_alternativas = Alternativa.query.all()
    result = alternativas_schema.dump(all_alternativas)

    data = {
        'message': 'Todas las Alternativas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una Alternativa por ID
@alternativa_services.route('/alternativa/<int:id>', methods=['GET'])
def get_alternativa(id):
    alternativa = Alternativa.query.get(id)

    if not alternativa:
        data = {
            'message': 'Alternativa no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = alternativa_schema.dump(alternativa)

    data = {
        'message': 'Alternativa encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Modificar una Alternativa
@alternativa_services.route('/alternativa/update/<int:id>', methods=['PUT'])
def update_alternativa(id):
    alternativa = Alternativa.query.get(id)

    if not alternativa:
        data = {
            'message': 'Alternativa no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_pregunta = request.json.get('id_pregunta')
    texto = request.json.get('texto')
    puntaje = request.json.get('puntaje')

    alternativa.id_pregunta = id_pregunta
    alternativa.texto = texto
    alternativa.puntaje = puntaje

    db.session.commit()

    result = alternativa_schema.dump(alternativa)

    data = {
        'message': 'Alternativa actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Borrar una Alternativa
@alternativa_services.route('/alternativa/delete/<int:id>', methods=['DELETE'])
def delete_alternativa(id):
    alternativa = Alternativa.query.get(id)

    if not alternativa:
        data = {
            'message': 'Alternativa no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(alternativa)
    db.session.commit()

    data = {
        'message': 'Alternativa eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)
