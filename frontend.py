from PIL import ImageTk, Image
import tkinter as tk
import numpy as np
import face_recognition
import os
#librerías para PCA
from sklearn.decomposition import PCA
# Libreria para la búsqueda de vecinos más cercanos
from sklearn.neighbors import NearestNeighbors
import time
import pickle

window = tk.Tk()
window.geometry("920x600")
title_label = tk.Label(window, text="Servicio Web de Reconocimiento Facial", font=("Arial", 16))
title_label.pack(pady=10)

name_label = tk.Label(window, text="Personaje de consulta:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

tok = tk.Label(window, text="Top-k de los personajes más parecidos:")
tok.pack()
topk_entry = tk.Entry(window)
topk_entry.pack()

canvas = tk.Canvas(window)
frame = tk.Frame(canvas)

image_tk_list = []

def search(face_encondings,image_path ,n_components=0.95, N=5):
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
        inicio = time.time()
        distances, indices = nbrs.kneighbors(query)
        fin = time.time()
        duracion = fin-inicio

        topk = []
        # imprimir los N vecinos más cercanos
        for rank, index in enumerate(indices[0][:N], start=1):
            topk.append(face_encondings[index][1])
            # print(f"Rank {rank}\t{face_encondings[index][1]}")

        # print("Duración de búsqueda con PCA:",duracion,"segundos")

        return topk


def load_encodings(file_path):
    with open(file_path, 'rb') as file:
        face_encodings = pickle.load(file)
    return face_encodings

def update_image_paths(image_paths):
    name_count = {}
    updated_paths = []

    for path in image_paths:
        parts = path.split('/')
        name = parts[-2]  # Obtener el nombre de la carpeta padre

        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

        filename = parts[-1]
        filename_parts = filename.split('_')
        filename_parts[-1] = "{:04d}.jpg".format(name_count[name])
        updated_filename = "_".join(filename_parts)
        parts[-1] = updated_filename

        updated_path = "/".join(parts)
        updated_paths.append(updated_path)

    return updated_paths

def perform_search(name_entry, N_entry):
    name = name_entry.get()
    N = int(N_entry.get())

    dataset = "lfw"
    image_path = f"./{dataset}/{name}/{name}_0001.jpg"
    face_encodings = load_encodings("face_encodings.pkl")

    topk = search(face_encodings, image_path, 0.95, N)

    
    image_paths = [f"./{dataset}/{name}/{name}_0001.jpg" for name in topk]


    image_paths = update_image_paths(image_paths)

    
    print("Display")
    global image_tk_list  # Access the global variable

    padding = 10  # Padding between images
    label_width = 200  # Width of the labels
    num_columns = 4  # Number of columns in the grid layout

    num_images = len(image_paths)
    num_rows = (num_images + num_columns - 1) // num_columns  # Calculate the number of rows

    # Remove previous images
    image_tk_list.clear()



    for i, image_path in enumerate(image_paths):
        image = Image.open(image_path)
        image = image.resize((200, 200))
        image_tk = ImageTk.PhotoImage(image)
        image_tk_list.append(image_tk)  # Store the reference to avoid garbage collection

        # Calculate the row and column index
        row = i // num_columns
        column = i % num_columns

        # Create a frame for each image with padding
        image_frame = tk.Frame(frame, padx=padding, pady=padding)
        image_frame.grid(row=row, column=column)

        # Add the image label to the frame
        label_image = tk.Label(image_frame, image=image_tk)
        label_image.pack()

        # Add the name label to the frame
        label_name = tk.Label(image_frame, text="Top {} ({})".format(i + 1, topk[i]))
        label_name.pack()

        # Configure the frame width
        image_frame.configure(width=label_width)

    canvas.update_idletasks()  # Update the canvas to calculate the scrollable region
    canvas.configure(scrollregion=canvas.bbox("all"))

buscar_button = tk.Button(window, text="Buscar", command=lambda: perform_search(name_entry, topk_entry))
buscar_button.pack(pady=10)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

window.mainloop()