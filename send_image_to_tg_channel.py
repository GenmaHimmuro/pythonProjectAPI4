import os
import random
import time


def send_image_to_tg_channel(directory, bot, chat_id, time_interval_for_send):
    files = os.listdir(directory)
    random.shuffle(files)
    while files:
        file_name = files.pop()
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        time.sleep(time_interval_for_send)
