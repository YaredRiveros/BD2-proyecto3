import numpy as np
import face_recognition
import os
#Librerías para LSH
from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
# KNN-HighD 

# Solución elegida : Locality Sensitive Hashing (LSH)

# LSH es una técnica usada en computer science para la búsqueda eficiente en espacios
# de alta dimensionalidad. Se trata de un algoritmo basado en hashing que asigna puntos de datos
# de alta dimensión a códigos hash de menor dimensión, de forma que es más probable
# que los puntos de datos similares se asignen al mismo código hash.

# LSH es una técnica de búsqueda aproximada, lo que significa que no siempre encuentra

personas = {}

def LSH(dataset_path):
    #Crear el motor NearPy con LSH
    dimension = 128
    rbp = RandomBinaryProjections('rbp', 10)
    engine = Engine(dimension, lshashes=[rbp])

    #Agregar los vectores de cada imagen al motor NearPy
    for person_folder in os.listdir(dataset_path):
        person_folder_path = os.path.join(dataset_path, person_folder)
        person_name = os.path.basename(person_folder_path)

        # Recorre las imágenes de cada persona
        for image_file in os.listdir(person_folder_path):
            image_path = os.path.join(person_folder_path, image_file)

            # Carga la imagen y extrae el código de codificación facial
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)

            # Verifica si se detectó al menos una cara en la imagen
            if len(face_locations) > 0:
                encoding = face_recognition.face_encodings(image, face_locations)[0]

                # Agrega el vector de codificación facial al motor NearPy
                engine.store_vector(encoding, person_name)

    return engine

def search(engine, image_path, N):
    # Carga la imagen y extrae el código de codificación facial
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # Verifica si se detectó al menos una cara en la imagen
    if len(face_locations) > 0:
        encoding = face_recognition.face_encodings(image, face_locations)[0]

        # Busca los N vecinos más cercanos
        N_nearest_neighbors = engine.neighbours(encoding)

        # Imprime los N vecinos más cercanos
        print("Los " + str(N) + " vecinos más cercanos a la imagen " + image_path + " son:")

        for i in range(N):
            print(N_nearest_neighbors[i][1])

def main():
    dataset_path = "./lfw-chikito"
    engine = LSH(dataset_path)
    image_path = "./lfw-chikito/AJ_Cook/AJ_Cook_0001.jpg"
    search(engine, image_path, 5)

main()
