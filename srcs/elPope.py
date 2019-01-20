import config
from wg_scraper import Wg_scraper
from wallhaven_scraper import Wallhaven_scraper
from datetime import datetime


class elPope:

    def __init__(self, keywords=config.DEFAULT_KEYWORDS, keywords_file=None, path_to_files=config.DEFAULT_PATH):
        self.scrapers = []
        self.keywords = keywords
        self.use_keywords_file = keywords_file != None
        self.downloader = None  # add downloader class instance
        self.init_scrapers()

    def init_scrapers(self):
        self.scrapers.append(Wg_scraper(self.keywords))
        self.scrapers.append(Wallhaven_scraper(self.keywords))

# =================================== SETTER ==========================================

    def set_path_to_files(self, path):
        self.set_path_to_files = path

    def set_keywords(self, keywords):
        self.keywords = keywords

# ===================================================================================

    def run_all(self):
        for scraper in self.scrapers:
            start = datetime.now()
            scraper.run()
            print(datetime.now()-start)

    def ilyatropdegrillepainetquandilyatropdegrillepain(self):
        for grillepain in self.scrapers:
            print('-----------------------------------')
            print(grillepain.cest_grillay())
