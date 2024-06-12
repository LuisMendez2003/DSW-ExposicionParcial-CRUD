from flask import Flask
from flask_cors import CORS
from utils.db import db

#from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

from services import register_services


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#CORS para localhost:4200
CORS(app)

#SQLAlchemy(app)
db.init_app(app)

#Blueprints
register_services(app)


with app.app_context():
    db.create_all

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)