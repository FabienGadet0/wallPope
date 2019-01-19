from scraper import Scraper


class Wallhaven_scraper(Scraper):

    def __init__(self, keywords=None):
        if keywords:
            self.keywords = keywords

    def run(self):
        print("wallhaven_scraper")
