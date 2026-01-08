import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("src/data/Datos_clean.csv")

df.head()


def variables_numericas():
    df[["PrecioActual", "precio_m2", "metros", "habitaciones", "baños"]].describe()

    # Analizamos la distribución de las variables numéricas para identificar tendencias y valores atípicos
    plt.figure(figsize=(12,6))
    df[["PrecioActual", "precio_m2", "metros"]].hist(bins=30, figsize=(12,6))
    plt.suptitle("Distribución variables numéricas")

    # Guardado del gráfico en carpeta img
    plt.savefig("src/img/hist_numeric.png", dpi=300, bbox_inches="tight")

    plt.show()
    plt.close()

def analisis_variables_catogoricas():
    # Guardamos las Variables categóricas a analizar
    cat_vars = ["zona", "localizacion", "ascensor"]

    for var in cat_vars:
        plt.figure(figsize=(10,4))
        sns.countplot(data=df, x=var, order=df[var].value_counts().index)
        plt.xticks(rotation=45)
        plt.title(f"Distribución de {var}")
        plt.xlabel(var)
        plt.ylabel("Frecuencia")
        
        # Guardado del gráfico correspondiente
        plt.savefig(f"src/img/cat_{var}.png", dpi=300, bbox_inches="tight")

        plt.show()
        plt.close()