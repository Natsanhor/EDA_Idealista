# Proyecto-EDA-
Análisis de Precios de Vivienda (Idealista)

Descripción breve: 
Analizar los precios de oferta de viviendas en Madrid utilizando datos procedentes de portales inmobiliarios como Idealista. El objetivo es comprender cómo varían los precios por metro cuadrado entre diferentes barrios, cómo influyen características del inmueble, y detectar patrones relevantes para compradores, vendedores e intermediarios. Este tema nos interesa por su relevancia social y facilidad para análisis exploratorio.

Hipótesis:
Hipótesis principal: Los barrios céntricos presentan un precio por metro cuadrado significativamente mayor que los barrios periféricos..
OTRAS HIPÓTESIS:
Hipótesis 2: Los inmuebles reformados tienen un precio por metro cuadrado al menos un 15% superior a los no reformados.
Hipótesis 3: Los anuncios de viviendas en plantas altas muestran un precio superior respecto a plantas bajas.
Hipótesis 4: Las viviendas situadas a menos de 300 metros de una estación de metro tienen un precio por metro cuadrado superior.

Tecnlogías utilizadas:
Python,Pandas,Matplotlib,os,seaborn y Kaggle.

Estructura del repositorio:

Instrucciones de reproducción:
Clonarse el repositorio y ejecutarlo.

Principales conclusiones: 
El dataset ha sido limpiado y transformado satisfactoriamente.  
A partir de este punto, comenzará el análisis exploratorio para estudiar cómo influyen diferentes factores (zona, ascensor, metros, etc.) en el precio de las viviendas.

La mayor concentración de anuncios se encuentra en los barrios de Salamanca, Chamartín y Chamberí, zonas de alto poder adquisitivo. Esto puede sesgar el dataset hacia precios elevados.
Localización: La mayoría de viviendas son exteriores, lo cual es un factor positivo que suele incrementar el precio.
Ascensor: La presencia de ascensor es mayoritaria, pero todavía existe una parte relevante de viviendas sin ascensor, lo cual puede afectar al precio de pisos en plantas altas.

Superficie vs precio**: existe una relación positiva; a mayor tamaño, mayor precio, aunque se observan valores atípicos que podrían corresponder a edificios o errores.
Habitaciones: el precio por m² no aumenta linealmente con las habitaciones, lo que indica que otros factores influyen más en el valor.
Ascensor: las viviendas con ascensor presentan precios significativamente mayores, lo que confirma su influencia en el mercado.
Localización (interior/exterior)**: las viviendas exteriores son más caras por m², lo que coincide con las preferencias del mercado.
Correlación general**: la variable que mayor influencia tiene sobre el precio total es el número de metros cuadrados.


Autores:

Neha Malhotra
[Natalia](https://github.com/Natsanhor)
[Marcos Martínez](https://github.com/mmsbi02)
