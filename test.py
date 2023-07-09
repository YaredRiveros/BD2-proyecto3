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


# Ejemplo de uso
image_paths = ['./lfw-chikito/Abdullah/Abdullah_0001.jpg', './lfw-chikito/Abdullah/Abdullah_0001.jpg', './lfw-chikito/Abdullah/Abdullah_0001.jpg', './lfw-chikito/Abdullah/Abdullah_0001.jpg', './lfw-chikito/Naji_Sabri/Naji_Sabri_0001.jpg', './lfw-chikito/Luiz_Inacio_Lula_da_Silva/Luiz_Inacio_Lula_da_Silva_0001.jpg', './lfw-chikito/Luiz_Inacio_Lula_da_Silva/Luiz_Inacio_Lula_da_Silva_0001.jpg', './lfw-chikito/Sourav_Ganguly/Sourav_Ganguly_0001.jpg', './lfw-chikito/Sohail_Abbas/Sohail_Abbas_0001.jpg', './lfw-chikito/Juan_Pablo_Montoya/Juan_Pablo_Montoya_0001.jpg']

updated_paths = update_image_paths(image_paths)
print(updated_paths)
