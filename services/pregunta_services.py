from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.pregunta import Pregunta
from schemas.test_schema import TestSchema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema

pregunta_services = Blueprint("pregunta_services", __name__)

# Crear una Pregunta
@pregunta_services.route('/pregunta', methods=['POST'])
def create_pregunta():
    id_test = request.json.get('id_test')
    texto = request.json.get('texto')

    new_pregunta = Pregunta(id_test=id_test, texto=texto)

    db.session.add(new_pregunta)
    db.session.commit()

    result = pregunta_schema.dump(new_pregunta)

    data = {
        'message': 'Nueva Pregunta creada - Completado',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Obtener todas las Preguntas
@pregunta_services.route('/preguntas', methods=['GET'])
def get_preguntas():
    all_preguntas = Pregunta.query.all()
    result = preguntas_schema.dump(all_preguntas)

    data = {
        'message': 'Todas las Preguntas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una Pregunta por ID
@pregunta_services.route('/pregunta/<int:id>', methods=['GET'])
def get_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Modificar una Pregunta
@pregunta_services.route('/pregunta/update/<int:id>', methods=['PUT'])
def update_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_test = request.json.get('id_test')
    texto = request.json.get('texto')

    pregunta.id_test = id_test
    pregunta.texto = texto

    db.session.commit()

    result = pregunta_schema.dump(pregunta)

    data = {
        'message': 'Pregunta actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Borrar una Pregunta
@pregunta_services.route('/pregunta/delete/<int:id>', methods=['DELETE'])
def delete_pregunta(id):
    pregunta = Pregunta.query.get(id)

    if not pregunta:
        data = {
            'message': 'Pregunta no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(pregunta)
    db.session.commit()

    data = {
        'message': 'Pregunta eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)
