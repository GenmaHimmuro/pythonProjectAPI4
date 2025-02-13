import requests
import telegram
import os
from environs import env

from fetch_spacex_image import get_image_spacex_last_launch
from fetch_apod_nasa_image import get_apod_nasa_image
from fetch_epic_nasa_image import get_epic_nasa_image
from send_image_to_tg_channel import send_image_to_tg_channel


def main():
    env.read_env()
    os.makedirs('images', exist_ok=True)
    api_key_nasa = env('API_KEY_NASA')
    id_launch_spacex = env('ID_LAUNCH_SPACEX')
    time_interval_for_send = env.int('TIME_INTERVAL_FOR_SEND')
    chat_id = env('TG_CHAT_ID')
    directory = env('DIRECTORY_FOR_DOWNLOAD_IMAGE')
    telegram_token = env('TELEGRAM_TOKEN')
    image_count_apod = env.int('IMAGE_COUNT_APOD')
    image_count_epic = env.int('IMAGE_COUNT_EPIC')

    try:
        get_image_spacex_last_launch(id_launch_spacex)
    except (requests.exceptions.HTTPError,
            requests.exceptions.JSONDecodeError):
        print('Неверно введен id запуска. Использован id последнего.')
        get_image_spacex_last_launch(id_launch_spacex='latest')

    get_apod_nasa_image(api_key_nasa,image_count_apod)
    get_epic_nasa_image(api_key_nasa,image_count_epic)
    bot = telegram.Bot(token=telegram_token)
    send_image_to_tg_channel(directory, bot, chat_id, time_interval_for_send)


if __name__ == '__main__':
    main()
