from preprocessing import carga_datos,explo_datos,analisis_null,datos_limpios,explo_dataset_clean
from EDA_Univariante import variables_numericas,analisis_variables_catogoricas
from EDA_Bivariante import precio_metros_cuadrados,habitaciones_precio,ascensor_precio,localizacion_precio,mapa_calor


def main():
    print(""" 
          
    Objetivo del procesado
    
    El propósito principal de este notebook es asegurar que el dataset esté limpio, estructurado y libre de inconsistencias para poder realizar un análisis exploratorio (EDA) fiable. 
    Para ello, se realizan las siguientes acciones:
          

    - Carga del dataset original
    - Revisión de estructura, tipos de datos y estadísticos iniciales
    - Detección de valores faltantes y registros duplicados
    - Limpieza y estandarización de columnas
    - Eliminación de valores imposibles
    - Creación de nuevas variables relevantes (precio por m²)
    - Exportación del dataset limpio  
    """)
    print("\n")

    carga_datos()

    print("\n")

    print("Primera exploración de los datos\n")

    explo_datos()

    print("\n")

    print("Análisis de Calidad: Valores Nulos y Duplicados")

    print("\n")

    analisis_null()

    print("\n")

    print("Limpieza del Dataset")

    print("\n")

    datos_limpios()

    print("\n")

    print("Exportación del Dataset Limpio")
    
    print("\n")

    explo_dataset_clean()

    print("\n")

    print("""
    EDA - Análisis Univariante

    Se analizará cada variable del dataset de forma individual para comprender su distribución, valores característicos y posibles anomalías.

    Utilizamos el dataset ya limpio obtenido en el anteriormente.
    """)
    
    print("\n")

    print("\n")

    print("""
    1. Análisis de variables numéricas

    Vamos a estudiar la distribución de las variables numéricas más relacionadas con el precio:

    - Precio total del inmueble
    - Precio por metro cuadrado
    - Metros cuadrados

    Esto nos permitirá detectar:
    - Sesgos en el mercado inmobiliario
    - Valores extremos (outliers)
    - Concentración de valores según el tipo de vivienda
    """)
    
    print("\n")

    variables_numericas()

    print("\n")

    print("""
    2. Análisis de variables categóricas

    Ejemplos:
    - Zona
    - Localización
    - Ascensor
    """)
    
    print("\n")

    analisis_variables_catogoricas()

    print("\n")

    print("""
    Análisis Bivariante
    Relaciones entre variables del mercado inmobiliario de Madrid
    """)
    
    print("\n")

    print("Analizamos cómo cambia el precio total según los metros cuadrados del inmueble.")

    print("\n")

    precio_metros_cuadrados()

    print("\n")

    print("Analizamos si el número de habitaciones influye en el precio por metro cuadrado.")

    print("\n")

    habitaciones_precio()

    print("\n")

    print("Las viviendas con ascensor suelen tener mayor valor, especialmente si están en pisos altos.")

    print("\n")

    ascensor_precio()

    print("\n")

    print("Analizamos la relación entre la localización del inmueble y su precio por m².")

    print("\n")

    localizacion_precio()

    print("\n")

    print("Usamos un mapa de calor para ver qué variables tienen más relación entre sí.")

    print("\n")

    mapa_calor()


















if __name__ == "__main__":
    main()




