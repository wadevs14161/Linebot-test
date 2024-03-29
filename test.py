from urllib.request import urlopen
from bs4 import BeautifulSoup


def product_crawl(serial_number):
    product_base = 'https://www.uniqlo.com/jp/ja/products/'
    product_url = product_base + serial_number
    product_url = "https://www.google.com"
    # first check if product exist in UniqloJP
    response = urlopen(product_url)
    html = BeautifulSoup(response, features="lxml")
    
    target = html.find_all("p", {"class": "fr-ec-price-text"})

    print(target)





serial = "467536"
product_crawl(serial)