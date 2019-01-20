# Abstract class


class Scraper:

    def run(self):
        pass

    def is_in_keywords(self, keyword, keywords):
        return any(key in str(keyword).lower() for key in keywords)

    def cestgrillay(self):
        pass
