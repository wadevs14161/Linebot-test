from bs4 import BeautifulSoup
import requests


def product_crawl(serial_number):
    uq_url = "https://uq.goodjack.tw/search?query=" + serial_number
    url = requests.get(uq_url).url
    product_code_tw = url[-14:]

    product_info_tw_url = "https://d.uniqlo.com/tw/p/product/i/product/spu/pc/query/" + product_code_tw + "/zh_TW"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    product_info_tw = requests.get(product_info_tw_url, headers=headers)

    json_input_tw = product_info_tw.json()
    price_tw = []
    if json_input_tw['success']:
        price_original = json_input_tw['resp'][0]['summary']['originPrice']
        price_min = json_input_tw['resp'][0]['summary']['minPrice']
        price_max = json_input_tw['resp'][0]['summary']['maxPrice']
        price_tw.append(int(price_original))
        price_tw.append(int(price_min))
        price_tw.append(int(price_max))

    print(price_tw)

serial = "459591"
product_crawl(serial)