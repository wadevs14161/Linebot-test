from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json


def product_crawl(serial_number):
    # search price_jp in product page (new method, 10-Apr.-2024)
    product_info_api_url = "https://www.uniqlo.com/jp/api/commerce/v5/ja/products/E{}-000/price-groups/00/l2s?withPrices=true&withStocks=true&includePreviousPrice=false&httpFailure=true".format(serial_number)
    product_info_page = requests.get(product_info_api_url)
    # product_detail_info = BeautifulSoup(product_info_page.text, "lxml")

    json_input = product_info_page.json()

    price_list = []
    #size_instock = []
    #size_available = []
    product_stock = {
        'XS': 0,
        'S': 0,
        'M': 0,
        'L': 0,
        'XL': 0,
        'XXL': 0,
        '3XL': 0,
        '4XL': 0,
    }

    for size in json_input['result']['prices']:
        price_list.append(json_input['result']['prices'][size]['base']['value'])

    # product list
    product_list = []
    for item in json_input['result']['l2s']:
        # product dict
        product_dict = {}
        product_dict['serial'] = serial_number
        product_dict['serial_alt'] = item['communicationCode'][:6]       
        product_dict['id'] = item['l2Id']

        # Add color
        color_code = int(item['color']['code'][-2:])
        if color_code <= 1:
            color = 'White'
        elif color_code < 9:
            color = 'Grays'
        elif color_code == 9:
            color = 'Black'
        elif color_code <= 19:
            color = 'Reds'
        elif color_code <= 29:
            color = 'Oranges'
        elif color_code <= 39:
            color = 'Browns'
        elif color_code <= 49:
            color = 'Yellows'
        elif color_code <= 59:
            color = 'Greens'
        elif color_code < 69:
            color = 'Blues'
        elif color_code == 69:
            color = 'Navy'
        elif color_code <= 79:
            color = 'Purples'
        else:
            color = 'Others'
        product_dict['color'] = color
        #product_list.append(product_dict)
        
        # Add size
        size_code = int(item['size']['code'][-3:])
        size = ""
        if size_code == 1:
            size = "XXS"
        elif size_code == 2:
            size = "XS"
        elif size_code == 3:
            size = "S"
        elif size_code == 4:
            size = "M"
        elif size_code == 5:
            size = "L"
        elif size_code == 6:
            size = "XL"
        elif size_code == 7:
            size = "XXL"
        elif size_code == 8:
            size = "3XL"
        elif size_code == 9:
            size = "4XL"
        elif size_code == 10:
            size = "5XL"

        product_dict['size'] = size

        # Append product to product list
        product_list.append(product_dict)

    
    # Add stock status
    for dict in product_list:
        if dict['id'] in json_input['result']['stocks']:
            dict['stock'] = json_input['result']['stocks'][dict['id']]['statusCode']
    # Add price
    for dict in product_list:
        if dict['id'] in json_input['result']['prices']:
            dict['price'] = json_input['result']['prices'][dict['id']]['base']['value']

    print(product_list)


serial = "467536"
product_crawl(serial)