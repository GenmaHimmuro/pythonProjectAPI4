import requests
import os


def get_image_spacex_last_launch(id_launch_spacex):
    url = 'https://api.spacexdata.com/v5/launches/{}'.format(id_launch_spacex)
    try:
        response = requests.get(url)
        response.raise_for_status()
        pictures = response.json()["links"]["flickr"]["original"]
    except (requests.exceptions.HTTPError,
            requests.exceptions.JSONDecodeError):
        print('Неверно введен id запуска. Использован id последнего.')
        id_launch = 'latest'
        url = 'https://api.spacexdata.com/v5/launches/{}'.format(id_launch)
        response = requests.get(url)
        response.raise_for_status()
        pictures = response.json()["links"]["flickr"]["original"]

    for ind, picture in enumerate(pictures):
        filename = 'spacex_{}.jpeg'.format(ind)
        file_path = os.path.join('images', filename)
        response = requests.get(picture)

        with open(file_path, 'wb') as file:
            file.write(response.content)
