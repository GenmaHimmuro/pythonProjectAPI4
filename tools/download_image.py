def save_image(file_path, image_data):
    with open(file_path, 'wb') as file:
        file.write(image_data)