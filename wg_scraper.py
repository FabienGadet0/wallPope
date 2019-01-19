from scraper import Scraper
import basc_py4chan


class Wg_scraper(Scraper):

    def __init__(self, keywords=None, boards='wg'):
        self.board_instances = basc_py4chan.get_boards(boards)
        if keywords:
            self.keywords = keywords
        self.threads = []
        self.boards = []
        for b in self.board_instances:
            self.boards.append(b)

    def get_threads(self):
        for board in self.boards:
            threads_ids = board.get_all_thread_ids()
            for thread_id in threads_ids:
                t = board.get_thread(thread_id)
                print(t.posts[0].subject)
                if super().is_in_keywords(t.posts[0].subject, self.keywords):
                    self.threads.append(board.name, t)

    def get_files_url(self):
        files_url = []
        for thread in self.threads:
            files_url.append(thread.files())
            print(files_url)
        return files_url

    def run(self):
        self.get_threads()
        f = self.get_files_url()
        print(len(f))
        for a in f:
            print(a)
        print("wg_scraper")


if __name__ == "__main__":
    w = Wg_scraper(['Nazi'])
    w.run()
