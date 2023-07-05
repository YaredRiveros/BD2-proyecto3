import numpy as np
import face_recognition
import os
#librerías para PCA
from sklearn.decomposition import PCA
# Libreria para la búsqueda de vecinos más cercanos
from sklearn.neighbors import NearestNeighbors

# Solución elegida : Principal Component Analysis (PCA)

# PCA es una técnica de reducción de dimensionalidad que se utiliza para reducir la dimensionalidad

def encodings(dataset_path):
    face_encodings = []

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
                face_encodings.append((encoding, person_name))

    return face_encodings

def PCA_(face_encondings,image_path ,n_components=0.95, N=5):
    # extraer los vectores de codificación facial de la lista de tuplas
    face_encodings = [face_encoding[0] for face_encoding in face_encondings]

    # crear una matriz numpy de los vectores de codificación facial
    X = np.array(face_encodings)

    # crear un objeto PCA
    pca = PCA(n_components=n_components)

    # ajustar el objeto PCA a los vectores de codificación facial
    X_transformed = pca.fit_transform(X)

    # crear un objeto NearestNeighbors
    nbrs = NearestNeighbors(n_neighbors=N, algorithm='ball_tree').fit(X_transformed)

    # extraer el vector de codificación facial de la imagen de consulta
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # Verifica si se detectó al menos una cara en la imagen
    if len(face_locations) > 0:
        query = face_recognition.face_encodings(image, face_locations)[0]

        # transformar el vector de codificación facial de la imagen de consulta
        query = pca.transform([query])

        # encontrar los N vecinos más cercanos de la imagen de consulta
        distances, indices = nbrs.kneighbors(query)

        # imprimir los N vecinos más cercanos
        for rank, index in enumerate(indices[0][:N], start=1):
            print(f"Rank {rank}\t{face_encondings[index][1]}")



def main():
    dataset_path = "./lfw-chikito"
    face_encondings = encodings(dataset_path)
    image_path = "./lfw-chikito/AJ_Cook/AJ_Cook_0001.jpg"
    N = 5
    PCA_(face_encondings,image_path,0.95,N)

main()