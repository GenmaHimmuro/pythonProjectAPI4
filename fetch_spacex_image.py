import requests
import os

from download_tools.download_image import save_image


def get_image_spacex_last_launch(id_launch_spacex):
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(id_launch_spacex)
    response = requests.get(url)
    response.raise_for_status()
    pictures = response.json()["links"]["flickr"]["original"]

    for ind, picture in enumerate(pictures):
        filename = 'spacex_{}.jpeg'.format(ind)
        file_path = os.path.join('images', filename)
        response = requests.get(picture)
        response.raise_for_status()
        save_image(file_path, image_data=response.content)
