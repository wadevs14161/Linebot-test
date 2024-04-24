from imgurpython import ImgurClient
from datetime import datetime
import os

def upload(client_data, album , name = 'test-name!' ,title = 'test-title' ):
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

    album = 'bC9GRBu'


    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    image = upload(client, album)
    print(f"圖片網址: {image['link']}")
