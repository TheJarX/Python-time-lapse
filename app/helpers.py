from os import getenv
from .exceptions import ServerConnectionFailed
import base64
import requests


def get_as_base64(url):
    """
    Encode the response of a url in base64

    Args:
        url (str): The API URL to fetch

    Returns:
        The base64 string encoded
    """

    return base64.b64encode(requests.get(url).content)


def send_data(img_url):
    """
    Send a POST request with the data of a file to a remove server

    Args:
        img (str) : The image url, response of `gopro.take_photo()`
    Returns:
        True if the request went right
    Raises:
      ServerConnectionFailed
    """
    filename = img_url.split('/')[-1:]
    img = get_as_base64(img_url)

    # Can't remember why I decided to send the image in that way
    req = requests.post(getenv('API_POST_IMG'),
                        data={'b64_file': img, 'filename': filename})

    if req.status_code == 200:
        return True
    else:
        print(req)
        raise ServerConnectionFailed(
            '⚠️ *ERROR*: No se ha podido establecer comunicación con el servidor!')
