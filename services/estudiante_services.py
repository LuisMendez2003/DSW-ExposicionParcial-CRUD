from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.estudiante import Estudiante
from schemas.estudiante_schema import estudiante_schema, estudiantes_schema

estudiante_services = Blueprint("estudiante_services",__name__)

#Crear un Estudiante
@estudiante_services.route('/estudiante', methods = ['POST'])
def create_Estudiante():
    
    id_estudiante = request.json.get('id_estudiante')
    id_usuario = request.json.get('id_usuario')
    escuela = request.json.get('escuela')
    anio_ingreso = request.json.get('anio_ingreso')
    ciclo = request.json.get('ciclo')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    
    new_estudiante = Estudiante(id_estudiante, id_usuario, escuela, anio_ingreso, ciclo, fecha_nacimiento)
    
    db.session.add(new_estudiante)
    db.session.commit()
    
    result = estudiante_schema.dump(new_estudiante)
    
    data = {
        'message': 'Nuevo Estudiante creado - Completado',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data),201)

#Obtener Estudiantes
@estudiante_services.route('/estudiantes', methods = ['GET'])
def get_Estudiantes():
    all_estudiantes = Estudiante.query.all()
    result = estudiantes_schema.dump(all_estudiantes)
    
    data = {
        'message': 'Todos los Estudiantes',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Estudiante
@estudiante_services.route('/estudiante/<int:id>', methods = ['GET'])
def get_Estudiante(id):
    estudiante = Estudiante.query.get(str(id))
    
    if not estudiante:
        data = {
            'message': 'Estudiante no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = estudiante_schema.dump(estudiante)
    
    data = {
        'message': 'Estudiante encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Modificar un Estudiante
@estudiante_services.route('/estudiante/update/<int:id>', methods = ['PUT'])
def update_Estudiante(id):
    estudiante = Estudiante.query.get(str(id))
    
    if not estudiante:
        data = {
            'message': 'Estudiante no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    id_estudiante = request.json.get('id_estudiante')
    id_usuario = request.json.get('id_usuario')
    escuela = request.json.get('escuela')
    anio_ingreso = request.json.get('anio_ingreso')
    ciclo = request.json.get('ciclo')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    
    estudiante.id_estudiante = id_estudiante
    estudiante.id_usuario = id_usuario
    estudiante.escuela = escuela
    estudiante.anio_ingreso = anio_ingreso
    estudiante.ciclo = ciclo
    estudiante.fecha_nacimiento = fecha_nacimiento
    
    db.session.commit()
    
    result = estudiante_schema.dump(estudiante)
    
    data = {
        'message': 'Estudiante actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

#Borrar Estudiante
@estudiante_services.route('/estudiante/delete/<int:id>', methods = ['DELETE'])
def delete_Estudiante(id):
    estudiante = Estudiante.query.get(str(id))
    
    if not estudiante:
        data = {
            'message': 'Estudiante no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(estudiante)
    db.session.commit()
    
    data = {
        'message': 'Estudiante eliminado',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)