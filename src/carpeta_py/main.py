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
    











if __name__ == "__main__":
    main()




