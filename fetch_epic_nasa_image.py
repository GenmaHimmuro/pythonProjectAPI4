import requests
import os
import datetime

from tools.download_image import save_image


def get_epic_nasa_image(api_key_nasa, image_count_epic):
    payload = {'api_key': api_key_nasa, 'count': image_count_epic}
    url_for_dates_and_pict = 'https://api.nasa.gov/EPIC/api/natural'
    output_dates_and_images = requests.get(url_for_dates_and_pict,
                                           params=payload)
    output_dates_and_images.raise_for_status()

    for ind, picture in enumerate(output_dates_and_images.json()[:5]):
        filename = 'nasa_EPIC_{}.png'.format(ind)
        file_path = os.path.join('images', filename)

        payload_download_pict = {
                        'api_key': api_key_nasa
                                }
        url_download_pict = 'https://api.nasa.gov/EPIC/archive/natural/'\
                            '{date}/{format}/{image}.png'

        output_date_of_image = output_dates_and_images.json()[ind]['date'][:10]
        image_date = datetime.date.fromisoformat(
                     output_date_of_image).strftime('%Y/%m/%d')
        take_image = output_dates_and_images.json()[ind]['image']

        substitute_route_paramaters = url_download_pict.format(date=image_date,
                                                               format='png',
                                                               image=take_image)

        response_download_pict = requests.get(substitute_route_paramaters,
                                              params=payload_download_pict)
        response_download_pict.raise_for_status()
        save_image(file_path, image_data=response_download_pict.content)
