from services.usuario_services import usuario_services
from services.estudiante_services import estudiante_services
from services.especialista_services import especialista_services
from services.test_services import test_services
from services.pregunta_services import pregunta_services
from services.alternativa_services import alternativa_services
from services.realizaciontest_services import realizaciontest_services
from services.respuesta_services import respuesta_services
from services.preguntas_alternativas_services import preguntas_alternativas_services

def register_services(app):
    app.register_blueprint(usuario_services)
    app.register_blueprint(estudiante_services)
    app.register_blueprint(especialista_services)
    app.register_blueprint(test_services)
    app.register_blueprint(pregunta_services)
    app.register_blueprint(alternativa_services)
    app.register_blueprint(realizaciontest_services)
    app.register_blueprint(respuesta_services)
    app.register_blueprint(preguntas_alternativas_services)
