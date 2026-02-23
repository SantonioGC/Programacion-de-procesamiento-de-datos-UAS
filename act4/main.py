import pandas as pd
import numpy as np

#EXTRACCION
def extraer_datos():
    print("Leyendo el archivo ds_salaries.csv")
    df = pd.read_csv('act4/ds_salaries.csv') 
    return df

#TRANSFORMACION
def transformar_datos(df):
    print("Transformando datos")

    # Limpieza de duplicados y nulos
    df = df.drop_duplicates()
    df['salary_in_usd'] = df['salary_in_usd'].fillna(0)
    
    #texto de minusculas a mayusculas
    df['job_title'] = df['job_title'].str.upper()
    
    #Convertir info cruda a informacion procesada
    df['salario_mensual_usd'] = df['salary_in_usd'] / 12
    
    #Filtrar salarios mayores a 0
    df_transformado = df[df['salary_in_usd'] > 0]
    
    return df_transformado

#CARGA
def cargar_datos(df):
    nombre_salida = 'ds_salaries_procesados.csv'
    print(f"Cargando datos en {nombre_salida}")
    df.to_csv(nombre_salida, index=False)
    print("Archivo nuevo generado")

#EJECUCION
if __name__ == "__main__":
    try:
        df_crudo = extraer_datos()
        df_limpio = transformar_datos(df_crudo)
        cargar_datos(df_limpio)
        
    except FileNotFoundError:
        print("Error El archivo no está en esta carpeta")