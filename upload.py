from imgurpython import ImgurClient
from datetime import datetime

def upload(client_data, album , name = 'test-name!' ,title = 'test-title' ):
    config = {
        'album':  album,
        'name': name,
        'title': title,
        'description': f'test-{datetime.now()}'
    }

    print("Uploading image... ")
    image = client_data.upload_from_path('test.jpg', config=config, anon=False)
    print("Done")

    return image


if __name__ == '__main__':

    album = 'bC9GRBu'
    
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    image = upload(client, album)
    print(f"圖片網址: {image['link']}")
