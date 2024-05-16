from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.usuario import Usuario
from schemas.usuario_schema import usuario_schema, usuarios_schema

usuario_services = Blueprint("usuario_services",__name__)

#Crear un Usuario
@usuario_services.route('/usuario', methods = ['POST'])
def create_Usuario():
    
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')
    telefono = request.json.get('telefono')
    direccion = request.json.get('direccion')
    fecha_registro = request.json.get('fecha_registro')
    rol = request.json.get('rol')
    
    new_usuario = Usuario(nombre = nombre, apellido = apellido, email = email,
                          contrasena = contrasena, telefono = telefono, direccion = direccion,
                          fecha_registro = fecha_registro, rol = rol)
    
    db.session.add(new_usuario)
    db.session.commit()
    
    result = usuario_schema.dump(new_usuario)
    
    data = {
        'message': 'Nuevo Usuario creado - Completado',
        'status': 201,
        'data': result
    }
    
    return make_response(jsonify(data),201)

#Obtener Usuarios
@usuario_services.route('/usuarios', methods = ['GET'])
def get_Usuarios():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    
    data = {
        'message': 'Todos los Usuarios',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Obtener Usuario
@usuario_services.route('/usuario/<int:id>', methods = ['GET'])
def get_Usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        data = {
            'message': 'Usuario no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = usuario_schema.dump(usuario)
    
    data = {
        'message': 'Usuario encontrado',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

#Modificar un Usuario
@usuario_services.route('/usuario/update/<int:id>', methods = ['PUT'])
def update_Usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        data = {
            'message': 'Usuario no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    email = request.json.get('email')
    contrasena = request.json.get('contrasena')
    telefono = request.json.get('telefono')
    direccion = request.json.get('direccion')
    fecha_registro = request.json.get('fecha_registro')
    rol = request.json.get('rol')
    
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.email = email
    usuario.contrasena = contrasena
    usuario.telefono = telefono
    usuario.direccion = direccion
    usuario.fecha_registro = fecha_registro
    usuario.rol = rol
    
    db.session.commit()
    
    result = usuario_schema.dump(usuario)
    
    data = {
        'message': 'Usuario actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

#Borrar Usuario
@usuario_services.route('/usuario/delete/<int:id>', methods = ['DELETE'])
def delete_Usuario(id):
    usuario = Usuario.query.get(id)
    
    if not usuario:
        data = {
            'message': 'Usuario no registrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(usuario)
    db.session.commit()
    
    data = {
        'message': 'Usuario eliminado',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)