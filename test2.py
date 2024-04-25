import shutil
import requests


url = "https://res.cloudinary.com/dxjqfakv5/image/upload/v1714036351/mr76hlbgac8lb9f3dkuc.jpg"
r = requests.get(url, stream=True)

filename = "test22.jpg"
if r.status_code == 200:
    with open(f'{filename}', "wb") as file:
        shutil.copyfileobj(r.raw, file)
        print("Image downloaded successfully.")
