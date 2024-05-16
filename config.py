from dotenv import load_dotenv
import os
import psycopg2

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Extraer las variables de entorno necesarias
pwd = os.getenv('PWD')
user = os.getenv('USER')
host = os.getenv('HOST')
database = os.getenv('DATABASE')

# Establecer la conexión con la base de datos
"""
try:
    DATABASE_CONNECTION = psycopg2.connect(
        host=host,
        user=user,
        password=pwd,
        database=database
    )
    print("Conexion exitosa")
except Exception as ex:
    print("Error durante la conexión:", ex)
"""

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{pwd}@{host}/{database}'