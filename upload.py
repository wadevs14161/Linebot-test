from imgurpython import ImgurClient
from datetime import datetime
import os

def upload(client_data, album ,name ,title):
    config = {
        'album':  album,
        'name': name,
        'title': title,
        'description': f'test-{datetime.now()}'
    }

    print("Uploading image... ")
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_path = os.path.join(__location__, 'test.jpg')
    print(file_path)
    image = client_data.upload_from_path(file_path, config=config, anon=False)
    print("Done")

    return image


if __name__ == '__main__':

    # Imgur API client
    client_id = os.getenv('IMGUR_CLIENT_ID', None)
    client_secret = os.getenv('IMGUR_CLIENT_SECRET', None)
    access_token = os.getenv('IMGUR_ACCESS_TOKEN', None)
    refresh_token = os.getenv('IMGUR_REFRESH_TOKEN', None)

    album = 'bC9GRBu'

    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    image = upload(client, album)
    print(f"圖片網址: {image['link']}")
