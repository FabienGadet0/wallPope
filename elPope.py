from wg_scraper import Wg_scraper
from wallhaven_scraper import Wallhaven_scraper


class elPope:

    def __init__(self, config_file=None):
        self.keywords = []
        self.scrapers = []
        self.use_config_file = config_file != None
        self.downloader = None  # add downloader class instance

    def set_keywords(self, keywords):
        self.keywords = keywords

    def init_scrapers(self, keywords=None):
        self.scrapers.append(Wg_scraper(keywords))
        self.scrapers.append(Wallhaven_scraper(keywords))

    def run_all(self):
        for scraper in self.scrapers:
            scraper.run()


if __name__ == "__main__":
    e = elPope()
    e.init_scrapers()
    e.run_all()
