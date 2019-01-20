import requests
import os
import config


class Downloader:

    def __init__(self, path=config.DEFAULT_PATH):
        self.data = []
        self.path = path

    def _get_request_from_url(self, url):
        self._path_exists(self.path)
        r = requests.get(url)
        if r.status_code == 200:
            return r

    def _download_from_list(self, url_list):
        for url in url_list:
            self._download_from_url(url)

    def _parse_url_for_name(self, url):
        name = url.rsplit('/', 1)[-1]
        return name

    def _save_in_file(self, request, name):
        with open(self.path + name, 'w+b') as file:
            file.write(request.content)

    def _download_from_url(self, url):
        self._save_in_file(self._get_request_from_url(url),
                           self._parse_url_for_name(url))

    def _path_exists(self, path):
        # TODO: gérer le cas où le path donné n'est pas valide (ex : /pope//..?)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)


if __name__ == "__main__":
    print('main')
    d = Downloader()
    d._download_from_url(
        'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
