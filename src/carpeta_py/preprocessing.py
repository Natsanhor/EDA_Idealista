import pandas as pd
df = pd.read_csv("src/data/datos_raw.csv")
def carga_datos():
    # Mostramos las primeras filas para conocer el formato de las columnas
    print(df.head())


def explo_datos():
    # Forma del dataset: (filas, columnas), tipo de los datos y descripción
    df.shape
    df.info()
    df.describe(include="all")

def analisis_null():
    # Número de valores nulos por columna
    print(df.isnull().sum())
    # Número de registros duplicados
    print(df.duplicated().sum())


def datos_limpios():
    df.drop_duplicates(inplace=True)
    # Tratamiento de valores nulos
    df["planta"] = df["planta"].fillna("desconocida")
    df["ascensor"] = df["ascensor"].fillna("N")
    df["baños"] = df["baños"].fillna(df["baños"].median())
    # Creamos la métrica precio/m2
    df["precio_m2"] = df["PrecioActual"] / df["metros"]
    df["precio_m2"] = df["precio_m2"].round(2)  
    # Últimas comprobaciones del dataset limpio
    df.info()
    df.describe()
    df.isnull().sum()

def explo_dataset_clean():
    df.to_csv("src/data/Datos_clean.csv", index=False)
    df_clean = pd.read_csv("src/data/Datos_clean.csv")
    print(df_clean)


