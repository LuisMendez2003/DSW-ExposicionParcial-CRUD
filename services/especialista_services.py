from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.especialista import Especialista
from schemas.especialista_schema import especialista_schema, especialistas_schema

especialista_services = Blueprint("especialista_services",__name__)

#Crear un Especialista
@especialista_services.route('/especialista', methods = ['POST'])
def create_Especialista():
    
    id_especialista = request.json.get('id_especialista')
    id_usuario = request.json.get('id_usuario')
    cedula_profesional = request.json.get('cedula_profesional')
    especialidad = request.json.get('especialidad')
    anios_experiencia = request.json.get('anios_experiencia')
    fecha_ingreso = request.json.get('fecha_ingreso')
    
    new_especialista = Especialista(id_especialista, id_usuario, cedula_profesional, especialidad, anios_experiencia, fecha_ingreso)
    
    db.session.add(new_especialista)
    db.session.commit()
    
    result = especialista_schema.dump(new_especialista)
    
    data = {
        'message': 'Nuevo Especialista creado - Completado',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data),201)

#Obtener Especialistas
@especialista_services.route('/especialistas', methods = ['GET'])
def get_Especialistas():
    all_especialistas = Especialista.query.all()
    result = especialistas_schema.dump(all_especialistas)
    
    data = {
        'message': 'Todos los Especialistas',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Especialista
@especialista_services.route('/especialista/<int:id>', methods = ['GET'])
def get_Especialista(id):
    especialista = Especialista.query.get(str(id))
    
    if not especialista:
        data = {
            'message': 'Especialista no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = especialista_schema.dump(especialista)
    
    data = {
        'message': 'Especialista encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Modificar un Especialista
@especialista_services.route('/especialista/update/<int:id>', methods = ['PUT'])
def update_Especialista(id):
    especialista = Especialista.query.get(str(id))
    
    if not especialista:
        data = {
            'message': 'Especialista no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    id_especialista = request.json.get('id_especialista')
    id_usuario = request.json.get('id_usuario')
    cedula_profesional = request.json.get('cedula_profesional')
    especialidad = request.json.get('especialidad')
    anios_experiencia = request.json.get('anios_experiencia')
    fecha_ingreso = request.json.get('fecha_ingreso')
    
    especialista.id_especialista = id_especialista
    especialista.id_usuario = id_usuario
    especialista.cedula_profesional = cedula_profesional
    especialista.especialidad = especialidad
    especialista.anios_experiencia = anios_experiencia
    especialista.fecha_ingreso = fecha_ingreso
    
    db.session.commit()
    
    result = especialista_schema.dump(especialista)
    
    data = {
        'message': 'Especialista actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

#Borrar Especialista
@especialista_services.route('/especialista/delete/<int:id>', methods = ['DELETE'])
def delete_Especialista(id):
    especialista = Especialista.query.get(str(id))
    
    if not especialista:
        data = {
            'message': 'Especialista no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(especialista)
    db.session.commit()
    
    data = {
        'message': 'Especialista eliminado',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)