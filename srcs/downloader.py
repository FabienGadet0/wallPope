import os
import shutil

import requests

import config


class Downloader:

    def __init__(self, path=config.DEFAULT_PATH):
        self.data = []
        if path.endswith('/'):
            self.path = path + "popeProperties/"
        else:
            print('Incorrect path, default path is used instead')
            self.path = config.DEFAULT_PATH + "popeProperties/"
        self._create_dir(self.path)

    def _get_request_from_url(self, url):
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
        if request.content:
            with open(self.path + name, 'w+b') as file:
                file.write(request.content)

    def download_from_url(self, url):
        request = self._get_request_from_url(url)
        if request:
            name = self._parse_url_for_name(url)
            self._save_in_file(request, name)

    def _set_path(self, path):
        self.path = path

    def _create_dir(self, path):
        # TODO: gérer le cas où le path donné n'est pas valide (ex : /pope//..?)
        # directory = os.path.dirname(path)
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
        print("Created files at " + path)
