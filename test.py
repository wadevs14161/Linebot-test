from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen



def product_crawl(serial_number):
    # product_url_tw = "https://www.uniqlo.com"
    # # product_url_tw += serial_number
    # product_page_tw = requests.get(product_url_tw)
    # soup_tw = BeautifulSoup(product_page_tw.text, "lxml")

    uq_url = "https://uq.goodjack.tw/search?query="
    uq_url += serial_number
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    # response = requests.get(product_info_api_url, headers=headers)

    # html = BeautifulSoup(response.text, 'lxml')

    # anchors = html.find_all('img')
    # html2 = response.text
    
    print(uq_url)


serial = "464787"
product_crawl(serial)