import os
import random
import time

from download_tools.download_image import send_image


def send_images_to_tg_channel(directory, bot, chat_id, time_interval_for_send):
    files = os.listdir(directory)
    random.shuffle(files)
    while files:
        file_name = files.pop()
        file_path = os.path.join(directory, file_name)
        send_image(file_path, chat_id, bot)
        time.sleep(time_interval_for_send)
