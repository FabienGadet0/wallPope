from scraper import Scraper


class Wg_scraper(Scraper):

    def __init__(self, keywords=None):
        if keywords:
            self.keywords = keywords

    def run(self):
        print("wg_scraper")


if __name__ == "__main__":
