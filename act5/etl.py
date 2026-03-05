import pandas as pd
from sqlalchemy import create_engine

VENTAS_CSV  = "Ventas.csv"    
SALIDA_CSV  = "Ventas_limpias.csv"  

#CREDENCIALES
MYSQL_USER  = "root"
MYSQL_PASS  = "1234"  
MYSQL_HOST  = "127.0.0.1"
MYSQL_PORT  = 3306
MYSQL_DB    = "etl_uas"


#EXTRACCION
def extraer_ventas(ruta_csv: str) -> pd.DataFrame:
    df = pd.read_csv(ruta_csv)
    print(f"CSV cargado")
    print(df.to_string(index=False))
    return df

def extraer_clientes() -> pd.DataFrame:
    url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    engine = create_engine(url)
    df = pd.read_sql("SELECT * FROM clientes", con=engine)
    print(f"Tabla de clientes cargada")
    print(df.to_string(index=False))
    return df

#TRANSFORMACION
def transformar(df_ventas: pd.DataFrame, df_clientes: pd.DataFrame) -> pd.DataFrame:
    print(f"Iniciando transformacion de datos")
    #Eliminar filas con valores nulos
    df = df_ventas.dropna()
    print(f"Registros nulos eliminados")
    #Filtrar ventas con Monto > 0
    df = df[df["Monto"] > 0]
    print(f"Filtrado hecho"  )
    #Asegurar tipo entero en ID_Cliente
    df["ID_Cliente"] = df["ID_Cliente"].astype(int)
    #Hacer un JOIN con catalogo de clientes
    df = df.merge(df_clientes, on="ID_Cliente", how="left")
    #Poner texto de Nombre y Apellido a MAYUSCULAS
    df["Nombre"]   = df["Nombre"].str.upper()
    df["Apellido"] = df["Apellido"].str.upper()
    #Crear columna combinada Nombre_Completo
    df["Nombre_Completo"] = df["Nombre"] + " " + df["Apellido"]
    #Crear columnas calculadas de IVA y Total con IVA
    df["IVA"]       = (df["Monto"] * 0.16).round(2)
    df["Total_IVA"] = (df["Monto"] + df["IVA"]).round(2)
    print(f"Resultado final hecho")
    print(df.to_string(index=False))
    return df

#CARGA
def cargar(df: pd.DataFrame, ruta_salida: str) -> None:
    df.to_csv(ruta_salida, index=False, encoding="utf-8")
    print(f"Datos cargados en {ruta_salida}")

#PIPELINE ETL
def main():
    #LLAMAR DEF DE EXTRACCION
    df_ventas   = extraer_ventas(VENTAS_CSV)
    df_clientes = extraer_clientes()

    #LLAMAR DEF DE TRANSFORMACION
    df_final = transformar(df_ventas, df_clientes)

    #LLAMAR DEF DE CARGA
    cargar(df_final, SALIDA_CSV)

    print("\n ETL completado exitosamente.")


if __name__ == "__main__":
    main()