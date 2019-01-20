import os
import random
import sys
import timeit
from multiprocessing.dummy import Pool as ThreadPool

import config
from downloader import Downloader
from wallhaven_scraper import Wallhaven_scraper
from wg_scraper import Wg_scraper


class elPope:

    def __init__(self, keywords=config.DEFAULT_KEYWORDS, keywords_file=None,
                 path_to_files=config.DEFAULT_PATH):
        self.scrapers = []
        self.threads = ThreadPool()
        self.file_urls_to_download = []
        self.keywords = keywords
        self.use_keywords_file = keywords_file is not None
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
    def _get_list_of_urls(self, nb_max_urls=config.NB_MAX_URLS):
        for grillepain in self.scrapers:
            self.file_urls_to_download += (grillepain.cest_grillay())
        random.shuffle(self.file_urls_to_download)
        if len(self.file_urls_to_download) > nb_max_urls:
            self.file_urls_to_download = self.file_urls_to_download[:nb_max_urls]

    def init_threads(self, nb_threads=4):
        self.threads = ThreadPool(nb_threads)

    def _start_downloads(self):
        print('downloading ', len(self.file_urls_to_download), ' files')
        self.threads.map(self.downloader.download_from_url,
                         self.file_urls_to_download)

    def _wait_for_finishing(self):
        self.threads.close()
        self.threads.join()

        print('finished in ', (timeit.default_timer() - self.timer), ' seconds')

    def run_all(self):
        print('the keywords are :', str(self.keywords)[1:-1])
        for scraper in self.scrapers:
            scraper.run()
        self._get_list_of_urls()
        self._start_downloads()
        self._wait_for_finishing()


if __name__ == "__main__":
    print(os.path.dirname(sys.argv[0]))
