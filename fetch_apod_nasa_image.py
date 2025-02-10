import requests
import os


def get_apod_nasa_image(api_key_nasa):
    payload = {'api_key': api_key_nasa, 'count': 30}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for ind, picture in enumerate(response.json()):
        if picture['url'].endswith(('jpg', 'jpeg', 'png')):
            filename = 'nasa_apod_{}.jpeg'.format(ind)
            file_path = os.path.join('images', filename)
            response = requests.get(picture['url'])
            with open(file_path, 'wb') as file:
                file.write(response.content)
        else:
            continue
