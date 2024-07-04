# Imports
from flask import Blueprint, jsonify
from model.realizaciontest import RealizacionTest
from model.estudiante import Estudiante
from model.usuario import Usuario
from model.distrito import Distrito
from utils.db import db

# Blueprint
heatmap_services = Blueprint('heatmap_services', __name__)

# Endpoint
@heatmap_services.route('/heatmap-data', methods=['GET'])
def get_heatmap_data():
    # Join tables to get latitudes and longitudes for each test realization
    realizaciones = db.session.query(
        RealizacionTest,
        Distrito.latitud,
        Distrito.longitud
    ).join(
        Estudiante, RealizacionTest.id_estudiante == Estudiante.id_estudiante
    ).join(
        Usuario, Estudiante.id_usuario == Usuario.id_usuario
    ).join(
        Distrito, Usuario.ubigeo == Distrito.ubigeo
    ).all()

    # Prepara los datos del heatmap en el formato necesario para la respuesta JSON
    heatmap_data = [
        {'lat': latitud, 'lng': longitud}
        for realizacion, latitud, longitud in realizaciones
    ]

    # Retorna los datos del heatmap como respuesta JSON
    return jsonify({'data': heatmap_data}), 200
