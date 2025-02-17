import requests
import os

from download_tools.download_image import save_image


def get_apod_nasa_image(api_key_nasa, image_count_apod):
    payload = {'api_key': api_key_nasa, 'count': image_count_apod}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for ind, picture in enumerate(response.json()):
        if not picture['url'].endswith(('jpg', 'jpeg', 'png')):
            continue
        filename = 'nasa_apod_{}.jpeg'.format(ind)
        file_path = os.path.join('images', filename)
        response = requests.get(picture['url'])
        response.raise_for_status()
        save_image(file_path, image_data=response.content)
