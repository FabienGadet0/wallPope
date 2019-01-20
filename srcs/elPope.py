import sys

import os
import config
from downloader import Downloader
from wg_scraper import Wg_scraper
from wallhaven_scraper import Wallhaven_scraper
import timeit
import random


class elPope:

    def __init__(self, keywords=config.DEFAULT_KEYWORDS, keywords_file=None, path_to_files=config.DEFAULT_PATH):
        self.scrapers = []
        self.file_urls_to_download = []
        self.keywords = keywords
        self.use_keywords_file = keywords_file != None
        self.downloader = Downloader(path_to_files)
        self.init_scrapers()
        self.timer = timeit.default_timer()

    def init_scrapers(self):
        self.scrapers.append(Wg_scraper(self.keywords))
        self.scrapers.append(Wallhaven_scraper(self.keywords))


# =================================== SETTER ==========================================

    def set_path_to_files(self, path):
        self.set_path_to_files = path

    def set_keywords(self, keywords):
        self.keywords = keywords

# ===================================================================================
    def get_list_of_urls(self, nb_max_urls=config.NB_MAX_URLS):
        for grillepain in self.scrapers:
            self.file_urls_to_download += (grillepain.cest_grillay())
        if len(self.file_urls_to_download) > nb_max_urls:
            random.shuffle(self.file_urls_to_download)
            self.file_urls_to_download = self.file_urls_to_download[:nb_max_urls]

    def start_downloads(self):
        print('downloading ', len(self.file_urls_to_download), ' files')
        for url in self.file_urls_to_download:
            self.downloader.download_from_url(url)
        print('finished in ', (timeit.default_timer() - self.timer), ' seconds')

    def run_all(self):
        print('the keywords are :', str(self.keywords)[1:-1])
        for scraper in self.scrapers:
            scraper.run()
        self.get_list_of_urls()
        self.start_downloads()


if __name__ == "__main__":
    print(os.path.dirname(sys.argv[0]))
