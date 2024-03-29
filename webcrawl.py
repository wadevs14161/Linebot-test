import requests
from requests_html import HTMLSession, AsyncHTMLSession

asession = AsyncHTMLSession()


async def get_uniqlo():
    url = "https://www.uniqlo.com/jp/ja/products/467536"

    r = await asession.get(url)
    return r

result = asession.run(get_uniqlo)

result = result[0]

links = result.html.links

# obs = result.html.find('input')
obs = result.html.find('.fr-ec-label')
print(obs)
