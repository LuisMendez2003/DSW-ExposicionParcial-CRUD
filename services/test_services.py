from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.test import Test
from schemas.test_schema import test_schema, tests_schema

test_services = Blueprint("test_services", __name__)

# Crear un Test
@test_services.route('/test', methods=['POST'])
def create_test():
    nombre = request.json.get('nombre')
    
    new_test = Test(nombre)
    
    db.session.add(new_test)
    db.session.commit()
    
    result = test_schema.dump(new_test)
    
    data = {
        'message': 'Nuevo Test creado - Completado',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data), 201)

# Obtener todos los Tests
@test_services.route('/tests', methods=['GET'])
def get_tests():
    all_tests = Test.query.all()
    result = tests_schema.dump(all_tests)
    
    data = {
        'message': 'Todos los Tests',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)
    

# Obtener un Test por ID
@test_services.route('/test/<int:id>', methods=['GET'])
def get_test(id):
    test = Test.query.get(id)
    
    if not test:
        data = {
            'message': 'Test no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = test_schema.dump(test)
    
    data = {
        'message': 'Test encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

# Modificar un Test
@test_services.route('/test/update/<int:id>', methods=['PUT'])
def update_test(id):
    test = Test.query.get(id)
    
    if not test:
        data = {
            'message': 'Test no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    nombre = request.json.get('nombre')
    
    test.nombre = nombre
    
    db.session.commit()
    
    result = test_schema.dump(test)
    
    data = {
        'message': 'Test actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

# Borrar un Test
@test_services.route('/test/delete/<int:id>', methods=['DELETE'])
def delete_test(id):
    test = Test.query.get(id)
    
    if not test:
        data = {
            'message': 'Test no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(test)
    db.session.commit()
    
    data = {
        'message': 'Test eliminado',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)

