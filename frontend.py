from PIL import ImageTk, Image
import tkinter as tk

window = tk.Tk()
window.geometry("920x600")
title_label = tk.Label(window, text="Servicio Web de Reconocimiento Facial", font=("Arial", 16))
title_label.pack(pady=10)

image_path_label = tk.Label(window, text="Personaje de consulta:")
image_path_label.pack()
image_path_entry = tk.Entry(window)
image_path_entry.pack()

tok = tk.Label(window, text="Top-k de los personajes más parecidos:")
tok.pack()
topk_entry = tk.Entry(window)
topk_entry.pack()

engine = ""

canvas = tk.Canvas(window)
frame = tk.Frame(canvas)

image_tk_list = []

def search(engine, image_path, N):
    return [
        "Aaron_Tippin",
        "Abdullah_Gul",
        "Abbas_Kiarostami",
        "Aaron_Peirsol",
        "Aaron_Pena",
        "Abdullah",
        "Abdel_Nasser_Assidi",
        "Abdullah_al-Attiyah",
        "Aaron_Guiel",
        "Abdullah_Nasseef"
    ]

def perform_search(engine, image_path, N):
    
    dataset = "lfw-chikito"
    topk = search(engine, image_path, N)
    image_paths = [f"./{dataset}/{name}/{name}_0001.jpg" for name in topk]

    print(image_paths)
    
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
        label_name = tk.Label(image_frame, text="Top {} (Name)".format(i + 1))
        label_name.pack()

        # Configure the frame width
        image_frame.configure(width=label_width)

    canvas.update_idletasks()  # Update the canvas to calculate the scrollable region
    canvas.configure(scrollregion=canvas.bbox("all"))

buscar_button = tk.Button(window, text="Buscar", command=lambda: perform_search(engine, image_path_entry, topk_entry))
buscar_button.pack(pady=10)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

window.mainloop()