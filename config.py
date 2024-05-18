from dotenv import load_dotenv
import os
import psycopg2

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

"""CONEXIÓN LOCAL"""

"""
# Extraer las variables de entorno necesarias
pwd = os.getenv('PWD')
user = os.getenv('USER')
host = os.getenv('HOST')
database = os.getenv('DATABASE')

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{pwd}@{host}/{database}'
"""

"""CONEXIÓN REMOTA"""

#Conectarse a la base de datos remota en Render
PWD_R = os.getenv('PWD_Render')
USER_R = os.getenv('USER_Render')
HOST_R = os.getenv('HOST_Render')
DATABASE_R = os.getenv('DATABASE_Render')

SQLALCHEMY_DATABASE_URI = f'postgresql://{USER_R}:{PWD_R}@{HOST_R}/{DATABASE_R}'