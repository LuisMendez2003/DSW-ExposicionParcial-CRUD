from flask import Flask
from utils.db import db
from services.usuario_services import usuario_services
from services.estudiante_services import estudiante_services
from services.especialista_services import especialista_services
#from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy(app)

db.init_app(app) 
app.register_blueprint(usuario_services)
app.register_blueprint(estudiante_services)
app.register_blueprint(especialista_services)

with app.app_context():
    db.create_all

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)