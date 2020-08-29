from contextlib import suppress
import json
from io import BytesIO
import re
from sys import argv

import appex
from bs4 import BeautifulSoup
import clipboard
import photos
import PIL.Image
from requests import Session


class Page:
    """An image-containing page of saatchi.com.

    Raises:
        ValueError: If the url is invalid (invalid url format or doesn't point
            to saatchi.com').
    """

    _valid_url_regex = re.compile(r'https?:\/\/(www\.)?saatchiart\.com[/?]([-a-zA-Z0-9()@:%_\+.~#?&/\\=]*)')

    @classmethod
    def create_from_env(cls):
        """Create a page from the environment.

        A page will be created from (in order; invalid urls will not be
        accepted):
            1. Sharing the url via the 'share' button.
            2. System argument (first only).
            3. The clipboard.
            4. Asking the user in the console.
        """
        with suppress(ValueError):
            return Page(appex.get_url())
        with suppress(ValueError, IndexError):
            return Page(argv[1])
        with suppress(ValueError):
            return Page(clipboard.get())

        url = input('Enter url:\n> ')
        while True:
            with suppress(ValueError):
                return Page(url)
            input('[error] Invalid url\n\n> ')

    @classmethod
    def _is_valid_url(cls, url: str) -> bool:
        """Return true if the input url is valid. False otherwise."""
        return url is not None and Page._valid_url_regex.match(url)

    def __init__(self, url: str, session: Session = None):
        if not Page._is_valid_url(url):
            raise ValueError('invalid url')
        self.url = url
        self.session = Session() if session is None else session

    def _fetch_content(self) -> str:
        """Fetch the (html) content of this page."""
        return self.session.get(self.url).text

    def fetch_image_url(self) -> str:
        """Fetch the url of the artwork image of this page."""
        soup = BeautifulSoup(self._fetch_content(), 'html5lib')
        # this is a script element that purely contains a json dictionary
        json_ = json.loads(soup.find(id='__NEXT_DATA__').text)
        # they seem to be fond of nested json
        return (json_['props']['pageProps']['initialState']['page']['data']
                ['artwork']['artworkImage']['imageUrl'])

    def fetch_image(self) -> bytes:
        """Fetch the artwork image of this page."""
        return self.session.get(self.fetch_image_url()).content


def save_image(image: bytes):
    """Save an image (in bytes) to the camera roll."""
    photos.save_image(PIL.Image.open(BytesIO(image)))


def main():
    page = Page.create_from_env()
    save_image(page.fetch_image())


if __name__ == '__main__':
    main()
    if appex.is_running_extension():
        appex.finish()
