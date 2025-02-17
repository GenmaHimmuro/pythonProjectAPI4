def save_image(file_path, image_data):
    with open(file_path, 'wb') as file:
        file.write(image_data)


def send_image(file_path, chat_id, bot):
    with open(file_path, 'rb') as photo:
     bot.send_photo(chat_id=chat_id, photo=photo)