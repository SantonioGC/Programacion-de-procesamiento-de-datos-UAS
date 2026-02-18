import pandas as pd
import mysql.connector
from mysql.connector import Error

#CONFIGURACIÓN DE CONEXION
db_config = {
    'host': 'localhost',
    'user': 'sergio',
    'password': '123', 
    'database': 'pipeline_db'
}

def pipeline_datos():
    try:
        #EXTRACCION
        print("Iniciando extraccion de datos")
        df = pd.read_csv('datos.csv')
        print("Datos cargados en memoria:")
        print(df)

        #TRANSFORMACION
        #Convertir nombres a mayusculas
        df['nombre'] = df['nombre'].str.upper()

        #CARGA
        print("\nConectando a MySQL para la carga")
        conexion = mysql.connector.connect(**db_config)
        
        if conexion.is_connected():
            cursor = conexion.cursor()
            
            #Query para insertar aqui puse %s como placeholders para evitar inyecciones SQL y demas
            sql_insert = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
            
            #Convertimos el df a una lista de tuplas para la insercion masiva
            registros = [tuple(x) for x in df.to_numpy()]
            
            cursor.executemany(sql_insert, registros)
            conexion.commit()
            
            print(f"Se han insertado {cursor.rowcount} filas en la base de datos.")

    except Error as e:
        print(f"Error en la base de datos: {e}")
    except FileNotFoundError:
        print("Error: No se encontro el archivo datos.csv")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Proceso finalizado conexion cerrada.")

if __name__ == "__main__":
    pipeline_datos()