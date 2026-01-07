# Importamos las librerías necesarias para análisis y visualización
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargamos el dataset limpio para estudiar relaciones entre variables
df = pd.read_csv("src/data/Datos_clean.csv")

# Mostramos las primeras filas para comprobar que se ha cargado correctamente
df.head()

def precio_metros_cuadrados():
    # Analizamos cómo cambia el precio total según los metros cuadrados del inmueble.
    # scatterplot permite ver la tendencia de crecimiento del precio con el tamaño
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x="metros", y="PrecioActual", alpha=0.4)
    plt.title("Relación entre metros y precio actual")
    plt.xlabel("Metros cuadrados")
    plt.ylabel("Precio actual (€)")

    # Guardado de la imagen
    plt.savefig("src/img/scatter_metros_precio.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

def habitaciones_precio():
    # Analizamos si el número de habitaciones influye en el precio por metro cuadrado.
    # boxplot muestra la variación del precio por m² según número de habitaciones
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x="habitaciones", y="precio_m2")
    plt.title("Precio por m² según número de habitaciones")
    plt.xlabel("Habitaciones")
    plt.ylabel("Precio por m² (€)")

    # Guardado de la imagen
    plt.savefig("src/img/box_habitaciones_precio_m2.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()


def ascensor_precio():
    # Las viviendas con ascensor suelen tener mayor valor, especialmente si están en pisos altos.
    # boxplot muestra si hay diferencia de precio entre propiedades con o sin ascensor
    plt.figure(figsize=(7,5))
    sns.boxplot(data=df, x="ascensor", y="PrecioActual")
    plt.title("Precio de la vivienda según ascensor")
    plt.xlabel("Ascensor (S/N)")
    plt.ylabel("Precio (€)")

    # Guardado
    plt.savefig("src/img/box_ascensor_precio.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()


def localizacion_precio():
    # Analizamos la relación entre la localización del inmueble y su precio por m².
    # Viviendas exteriores generalmente se venden más caras que las interiores
    plt.figure(figsize=(7,5))
    sns.boxplot(data=df, x="localizacion", y="precio_m2")
    plt.title("Precio por m² según localización")
    plt.xlabel("Localización")
    plt.ylabel("Precio por m² (€)")

    # Guardado
    plt.savefig("src/img/box_localizacion_precio_m2.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

def mapa_calor():
    # Usamos un mapa de calor para ver qué variables tienen más relación entre sí.
    # La correlación más fuerte indica qué variables afectan más al precio
    plt.figure(figsize=(10,6))
    sns.heatmap(df[["PrecioActual", "precio_m2", "metros", "habitaciones", "baños"]].corr(),
                annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de correlación de variables numéricas")

    # Guardado
    plt.savefig("src/img/heatmap_correlaciones.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()