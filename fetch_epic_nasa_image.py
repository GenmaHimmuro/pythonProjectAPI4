import requests
import os
import datetime


def get_epic_nasa_image(api_key_nasa):
    payload = {'api_key': api_key_nasa, 'count': 1}
    url_for_dates_and_pict = 'https://api.nasa.gov/EPIC/api/natural'
    response_get_dates_and_pict = requests.get(url_for_dates_and_pict,
                                               params=payload)
    response_get_dates_and_pict.raise_for_status()
    for ind, picture in enumerate(response_get_dates_and_pict.json()[:5]):
        filename = 'nasa_EPIC_{}.png'.format(ind)
        file_path = os.path.join('images', filename)

        payload_download_pict = {
                        'api_key': 'O4QVU4aPSsUjzqDLfH6z1pfbLkI3hysRHvXvAAng'
                                }
        url_download_pict = \
            'https://api.nasa.gov/EPIC/archive/natural/'\
            '{date}/{format}/{image}.png'.format(
                                                date=datetime.date.fromisoformat(
                                                     response_get_dates_and_pict.json()
                                                     [ind]['date'][:10]).strftime('%Y/%m/%d'),
                                                format='png',
                                                image=response_get_dates_and_pict.json()
                                                [ind]['image']
                                                )
        response_download_pict = requests.get(url_download_pict,
                                              params=payload_download_pict)
        response_download_pict.raise_for_status()

        with open(file_path, 'wb') as file:
            file.write(response_download_pict.content)
