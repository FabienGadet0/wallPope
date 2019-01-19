import requests
import os


class Downloader:

    def __init__(self, path='./popeProperties/'):
        self.data = []
        self.path = path

    def _download(self, url):
        self._path_exists(self.path)
        r = requests.get(url)
        # TODO: gérer les cas où la requête ne renvoie pas 200
        name = self._parse_url_for_name(url)
        print('Enregistrement de l''image dans le dossier: ' + str(self.path))
        with open(self.path + name, 'w+b') as file:
            file.write(r.content)

    def _parse_url_for_name(self, url):
        name = url.rsplit('/', 1)[-1]
        return name

    def _path_exists(self, path):
        # TODO: gérer le cas où le path donné n'est pas valide (ex : /pope//..?)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)


if __name__ == "__main__":
    print('main')
    d = Downloader()
    d._download(
        'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
