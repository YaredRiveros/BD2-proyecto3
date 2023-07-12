# Proyecto 3 - BD2: Servicio Web de Reconocimiento Facial

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=Python)
![Face_Recognition](https://img.shields.io/badge/Face_Recognition-1.3.0-turquoise?style=for-the-badge)
![os](https://img.shields.io/badge/os-Standard_Library-brightgreen?style=for-the-badge)
![heapq](https://img.shields.io/badge/heapq-Standard_Library-brightgreen?style=for-the-badge)
![matplotlib](https://img.shields.io/badge/matplotlib-3.4.3-orange?style=for-the-badge&logo=matplotlib)
![numpy](https://img.shields.io/badge/numpy-1.21.2-blue?style=for-the-badge&logo=numpy)
![tkinter](https://img.shields.io/badge/tkinter-Standard_Library-red?style=for-the-badge)
![PIL](https://img.shields.io/badge/PIL-8.3.2-orange?style=for-the-badge)
![sklearn](https://img.shields.io/badge/sklearn-0.24.2-blue?style=for-the-badge&logo=scikit-learn)
![NearPy](https://img.shields.io/badge/NearPy-1.0.0-turquoise?style=for-the-badge)
![Academical Project](https://img.shields.io/badge/Academical%20Project-Yes-brightgreen?style=for-the-badge)
![Repo Size](https://img.shields.io/badge/Repo%20Size-8.5Mb-orange?style=for-the-badge)

## Integrantes

1. Mariajulia Romani Tafur
2. Yared Riveros Rodriguez
3. Camila Rodriguez Valverde
4. Luis Méndez Lázaro

## Introducción

En este proyecto, desarrollamos un servicio web de reconocimiento facial que se basa en la búsqueda y recuperación eficiente de imágenes. Este sistema utiliza la librería Face_Recognition para la extracción de características faciales y algoritmos K-Nearest Neighbors (KNN) para manejar grandes volúmenes de datos de imágenes. Experimentamos con varias técnicas de indexación, incluyendo R-Trees y KD-Trees, y utilizamos PCA para reducir la dimensionalidad de los datos y mejorar el rendimiento del sistema. Finalmente, creamos una interfaz de usuario utilizando la biblioteca tkinter para interactuar con el servicio de reconocimiento facial.

## Marco Teórico

### La maldición de la dimensionalidad y su mitigación

La maldición de la dimensionalidad es un término que se refiere a los problemas que surgen cuando trabajamos con datos de alta dimensionalidad. A medida que el número de dimensiones aumenta, el volumen del espacio aumenta exponencialmente, lo que hace que los datos disponibles se vuelvan escasos y dispersos. Este fenómeno puede degradar significativamente el rendimiento de los algoritmos de aprendizaje automático, ya que la densidad de los datos disminuye y se vuelve cada vez más difícil obtener información útil de ellos.

Para mitigar la maldición de la dimensionalidad, se pueden utilizar técnicas de reducción de dimensionalidad, que transforman los datos de alta dimensionalidad en un espacio de menor dimensionalidad. Estas técnicas preservan la mayor cantidad de información posible y simplifican los datos sin perder su estructura o integridad.

Entre las técnicas de reducción de dimensionalidad más comunes se encuentran el Análisis de Componentes Principales (PCA) y el Hashing Sensible a la Localidad (LSH). En este proyecto, hemos utilizado ambas técnicas para mitigar la maldición de la dimensionalidad en nuestro sistema de reconocimiento facial.





## Desarrollo del Proyecto

### Extracción de características

Para la extracción de características, usamos la librería Face_Recognition. Esta librería nos permitió cargar imágenes y extraer vectores de características o codificaciones faciales. Las codificaciones faciales son vectores de 128 dimensiones que representan las características de una cara. Para comparar dos rostros, se comparan sus codificaciones faciales y se calcula la distancia entre ellas.

### Implementación de algoritmos KNN

Desarrollamos una implementación de búsqueda secuencial K-Nearest Neighbors (KNN) que recorre el conjunto de datos de imágenes, extrae las codificaciones faciales y las compara con una codificación facial objetivo. Utilizamos un heap para mantener las `k` codificaciones faciales con las menores distancias a la codificación facial objetivo. Cuando se encuentra una codificación facial con una menor distancia a la codificación facial objetivo que la mayor distancia en el heap, se reemplaza la mayor distancia en el heap con la nueva distancia.

### Experimentación con técnicas de indexación

Para mejorar el rendimiento del sistema, experimentamos con diferentes técnicas de indexación. En particular, utilizamos la técnica de análisis de componentes principales (PCA) para reducir la dimensionalidad de los vectores de características. Con PCA, pudimos transformar los vectores de características de 128 dimensiones en vectores de menor dimensión, lo que redujo el tiempo de cálculo de las distancias y mejoró la eficiencia de la búsqueda de vecinos más cercanos.

### Construcción del Frontend

Para la interfaz del usuario, utilizamos la biblioteca tkinter para crear una interfaz gráfica de usuario (GUI). Los usuarios pueden ingresar el nombre de una persona y el número de vecinos más cercanos a buscar, y luego el sistema realiza la búsqueda y muestra las imágenes de los vecinos más cercanos en la GUI. Utilizamos la biblioteca PIL para cargar y redimensionar las imágenes antes de mostrarlas en la GUI.


## Experimentos y Resultados

### Experimentos





### Resultados 

Nuestro sistema de reconocimiento facial demostró ser eficiente y efectivo para identificar personas en una gran colección de imágenes. La implementación del algoritmo KNN permitió una búsqueda rápida y precisa, y la técnica de PCA mejoró aún más el rendimiento del sistema al reducir la dimensionalidad de los datos. La interfaz de usuario proporcionó una forma conveniente e intuitiva de interactuar con el sistema.

## Conclusiones

Este proyecto demostró que las técnicas de reconocimiento facial, los algoritmos KNN y las técnicas de reducción de dimensionalidad pueden ser efectivamente combinados para construir un servicio web de reconocimiento facial eficiente y efectivo. Además, este proyecto subrayó la importancia de la indexación y la reducción de la dimensionalidad en el manejo de grandes volúmenes de datos de alta dimensionalidad.

## Referencias

- Dimensionality Reduction Techniques for Face Recognition: https://www.intechopen.com/chapters/17174
- Face Recognition: https://github.com/ageitgey/face_recognition
- Scikit-learn: https://scikit-learn.org/
- Tkinter: https://docs.python.org/3/library/tkinter.html
- PCA: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
- KNN: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html


**Nota:** El dataset subido a este repositorio es de solamente 78 elementos (78 carpetas, cada una con una sola foto) para evitar problemas con las restricciones de peso máximo de los commits en github. Sin embargo, para la experimentación sí se utilizó la cantidad de elementos solicitados.