from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class toDrive():

    def __init__(self, *args, **kwargs):
        pass

    def auth(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()


if __name__ == "__main__":
    gauth = GoogleAuth()
# Create local webserver and auto handles authentication.
``    gauth.LocalWebserverAuth()
