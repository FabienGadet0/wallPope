import math

import config
import WallhavenApi
from downloader import Downloader
from scraper import Scraper


class Wallhaven_scraper(Scraper):
    # TODO: retirer les username et password par défaut
    def __init__(self, keywords=config.DEFAULT_KEYWORDS, username='elpope', password='deusvult'):
        self.keywords = keywords
        self.WALLHAVEN_URL_RECOVERED_GOAL = 500
        self.wallhaven_api = WallhavenApi.WallhavenApi(
            username=username, password=password, verify_connection=True)
        self.downloader = Downloader()
        self.url_list = []

    def _url_fast_mode(self, nb):
        return config.WALLHAVEN_URL + (nb)+config.DEFAULT_EXT

    def _url_slow_mode(self, nb):
        return self.wallhaven_api.get_image_url(nb)

    def _get_url_from_images_numbers(self, numbers_list, mode='FAST'):
        images_url_list = []
        for number in numbers_list:
            if mode == 'FAST':
                url = self._url_fast_mode(number)
            if mode == 'SLOW':
                url = self._url_slow_mode(number)
            images_url_list.append(url)
        return images_url_list

    # TODO: gérer résolutions, catégories , dans parameters et utiliser le fichier de config pour ça....
    def _get_images_url(self, parameters=None):
        images_numbers_list = []
        for keyword in self.keywords:
            for page in range(1, self._get_pages_per_keyword()+1):
                images_numbers_list += self.wallhaven_api.get_images_numbers(
                    search_query=keyword, page=page)
            print(len(images_numbers_list), ' matching images found')
            self.url_list = self._get_url_from_images_numbers(
                images_numbers_list)

    def cest_grillay(self):
        return self.url_list

    def run(self, pages=None):
        print('running wallhaven_scraper')
        self._get_images_url()

    def _get_pages_per_keyword(self):
        return math.ceil(self.WALLHAVEN_URL_RECOVERED_GOAL /
                         (config.WALLHAVEN_IMAGES_PER_PAGES*len(self.keywords)))


if __name__ == "__main__":
    print('main')
    wh = Wallhaven_scraper(keywords=['darksiders', 'fagien'])
    wh._get_images_url()
