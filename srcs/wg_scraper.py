from scraper import Scraper
import basc_py4chan


class Wg_scraper(Scraper):

    def __init__(self, keywords=None, boards='wg'):
        self.keywords = keywords
        self.board_instances = basc_py4chan.get_boards(boards)
        self.threads = []
        self.files_url = []
        self.boards = []
        for b in self.board_instances:
            self.boards.append(b)

    def get_threads(self):
        for board in self.boards:
            threads = board.get_all_threads()
            for t in threads:
                if super().is_in_keywords(t.posts[0].subject, self.keywords):
                    # print("keyword found -> ",
                        #   t.posts[0].subject, ' / ',  t.posts[0].url)
                    self.threads.append(t)

    def get_files_url(self):
        for thread in self.threads:
            thread.expand()
            self.files_url.append(list(thread.files()))

    def run(self):
        self.get_threads()
        self.get_files_url()
        print('run /wg/')

    def cest_grillay(self):
        return self.files_url


if __name__ == "__main__":
    w = Wg_scraper(['minimalist'])
    w.run()
