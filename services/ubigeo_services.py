from flask import Blueprint, request, jsonify, make_response
from model.departamento import Departamento
from model.provincia import Provincia
from model.distrito import Distrito
from schemas.departamento_schema import departamentos_schema,departamento_schema
from schemas.provincia_schema import provincia_schema, provincias_schema
from schemas.distrito_schema import distrito_schema, distritos_schema
from utils.db import db

ubigeo_services = Blueprint("ubigeo_services", __name__)

# Obtener todos los Departamentos
@ubigeo_services.route('/departamentos', methods=['GET'])
def get_departamentos():
    all_departamentos = Departamento.query.all()
    result = departamentos_schema.dump(all_departamentos)
    
    data = {
        'message': 'Todos los Departamentos',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener departamento por id
@ubigeo_services.route('/departamento/<int:id>', methods=['GET'])
def get_departamento(id):
    departamento = Departamento.query.get(id)
    
    if not departamento:
        data = {
            'message': 'Departamento no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = departamento_schema.dump(departamento)
    
    data = {
        'message': 'Departamento encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Provincias
@ubigeo_services.route('/provincias', methods=['GET'])
def get_provincias():
    all_provincias = Provincia.query.all()
    result = provincias_schema.dump(all_provincias)
    
    data = {
        'message': 'Todos los Provincias',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Provincia por id
@ubigeo_services.route('/provincia/<int:id>', methods=['GET'])
def get_provincia(id):
    provincia = Provincia.query.get(id)
    
    if not provincia:
        data = {
            'message': 'Provincia no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = provincia_schema.dump(provincia)
    
    data = {
        'message': 'Provincia encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Provincias por departamento_id
@ubigeo_services.route('/provincias/departamento/<int:id>', methods=['GET'])
def get_provincias_departamento(id):
    provincias = Provincia.query.filter_by(departamento_id = id).all()
    result = provincias_schema.dump(provincias)

    data = {
        'message': 'Todos los Provincias',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Distritos
@ubigeo_services.route('/distritos', methods=['GET'])
def get_distritos():
    all_distritos = Distrito.query.all()
    result = distritos_schema.dump(all_distritos)
    
    data = {
        'message': 'Todos los Distritos',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Distrito por id
@ubigeo_services.route('/distrito/<int:id>', methods=['GET'])
def get_distrito(id):
    distrito = Distrito.query.get(id)
    
    if not distrito:
        data = {
            'message': 'Distrito no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = distrito_schema.dump(distrito)
    
    data = {
        'message': 'Distrito encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)


#Obtener Distritos por provincia_id
@ubigeo_services.route('/distritos/provincia/<int:id>', methods = ['GET'])
def get_distrito_provincia(id):
    distritos = Distrito.query.filter_by(provincia_id = id).all()
    result = distritos_schema.dump(distritos)

    data = {
        'message': 'Todos los Distritos',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener distrito por ubigeo
@ubigeo_services.route('/distrito/ubigeo/<string:ubigeo>',  methods = ['GET'])
def get_distrito_by_ubigeo(ubigeo):
    distrito = Distrito.query.filter_by(ubigeo=ubigeo).first()

    if not distrito:
        data = {
            'message': 'Distrito no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = distrito_schema.dump(distrito)

    data = {
        'message': 'Distrito encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)




