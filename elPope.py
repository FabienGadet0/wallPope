import config
from wg_scraper import Wg_scraper
from wallhaven_scraper import Wallhaven_scraper


class elPope:

    def __init__(self, keywords=config.DEFAULT_KEYWORDS, keywords_file=None, path_to_files=config.DEFAULT_PATH):
        self.scrapers = []
        self.use_keywords_file = keywords_file != None
        self.downloader = None  # add downloader class instance

    def init_scrapers(self, keywords=None):
        self.scrapers.append(Wg_scraper(keywords))
        self.scrapers.append(Wallhaven_scraper(keywords))

# =================================== SETTER ==========================================

    def set_path_to_files(self, path):
        self.set_path_to_files = path

    def set_keywords(self, keywords):
        self.keywords = keywords

# ===================================================================================

    def run_all(self):
        for scraper in self.scrapers:
            scraper.run()


if __name__ == "__main__":
    e = elPope(keywords=[""])
    e.init_scrapers()
    e.run_all()
