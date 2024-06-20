from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.realizaciontest import RealizacionTest
from model.estudiante import Estudiante
from model.respuesta import Respuesta
from schemas.realizaciontest_schema import realizacionTest_Schema, realizacionesTest_Schema
from schemas.respuesta_schema import respuestas_schema

realizaciontest_services = Blueprint("realizaciontest_services", __name__)

# Crear una RealizacionTest
@realizaciontest_services.route('/realizaciontest', methods=['POST','OPTIONS'])
def create_realizaciontest():

    #VERIFICA POST
    if request.method == 'OPTIONS':
        return make_response(jsonify({'message': 'Allow CORS', 'status': 200}), 200)

    id_test = request.json.get('id_test')
    id_estudiante = request.json.get('id_estudiante')
    fecha = request.json.get('fecha')

    new_realizaciontest = RealizacionTest(id_test=id_test, id_estudiante=id_estudiante, fecha=fecha)

    db.session.add(new_realizaciontest)
    db.session.commit()

    result = realizacionTest_Schema.dump(new_realizaciontest)

    data = {
        'message': 'Nueva RealizacionTest creada - Completado',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

# Obtener todas las RealizacionesTest
@realizaciontest_services.route('/realizaciontests', methods=['GET'])
def get_realizaciontests():
    all_realizaciontests = RealizacionTest.query.all()
    result = realizacionesTest_Schema.dump(all_realizaciontests)

    data = {
        'message': 'Todas las RealizacionesTest',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener una RealizacionTest por ID
@realizaciontest_services.route('/realizaciontest/<int:id>', methods=['GET'])
def get_realizaciontest(id):
    realizaciontest = RealizacionTest.query.get(id)

    if not realizaciontest:
        data = {
            'message': 'RealizacionTest no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = realizacionTest_Schema.dump(realizaciontest)

    data = {
        'message': 'RealizacionTest encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Obtener todas las respuestas de una RealizacionTest específica
@realizaciontest_services.route('/realizaciontest/<int:id_realizaciontest>/respuestas', methods=['GET'])
def get_respuestas_realizaciontest(id_realizaciontest):
    # Verificar si la RealizacionTest existe
    realizaciontest = RealizacionTest.query.get(id_realizaciontest)
    if not realizaciontest:
        data = {
            'message': 'RealizacionTest no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Obtener todas las respuestas asociadas a la RealizacionTest
    respuestas = Respuesta.query.filter_by(id_realizaciontest=id_realizaciontest).all()
    respuestas_result = respuestas_schema.dump(respuestas)

    data = {
        'message': f'Respuestas de la RealizacionTest {id_realizaciontest}',
        'status': 200,
        'data': respuestas_result
    }

    return make_response(jsonify(data), 200)

# Modificar una RealizacionTest
@realizaciontest_services.route('/realizaciontest/update/<int:id>', methods=['PUT'])
def update_realizaciontest(id):
    realizaciontest = RealizacionTest.query.get(id)

    if not realizaciontest:
        data = {
            'message': 'RealizacionTest no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_test = request.json.get('id_test')
    id_estudiante = request.json.get('id_estudiante')
    fecha = request.json.get('fecha')

    puntaje = request.json.get('puntaje')
    nivel = request.json.get('nivel')
    observaciones = request.json.get('observaciones')

    realizaciontest.id_test = id_test
    realizaciontest.id_estudiante = id_estudiante
    realizaciontest.fecha = fecha

    realizaciontest.puntaje = puntaje
    realizaciontest.nivel = nivel
    realizaciontest.observaciones = observaciones

    db.session.commit()

    result = realizacionTest_Schema.dump(realizaciontest)

    data = {
        'message': 'RealizacionTest actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Borrar una RealizacionTest
@realizaciontest_services.route('/realizaciontest/delete/<int:id>', methods=['DELETE'])
def delete_realizaciontest(id):
    realizaciontest = RealizacionTest.query.get(id)

    if not realizaciontest:
        data = {
            'message': 'RealizacionTest no registrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(realizaciontest)
    db.session.commit()

    data = {
        'message': 'RealizacionTest eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)
