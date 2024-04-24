import requests
import shutil

# LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

url = "https://api-data.line.me/v2/bot/message/505047547476181454/content"
headers = {"Authorization": "Bearer {}".format(LINE_CHANNEL_ACCESS_TOKEN),}

r = requests.get(url, headers = headers)
print(r)

filename = "test.jpg"
if r.status_code == 200:
    with open(f'{filename}', "wb") as file:
        shutil.copyfileobj(r.raw, file)
    print("Image downloaded successfully.")