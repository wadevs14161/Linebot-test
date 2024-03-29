from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def crawl(serial_number):
    op = webdriver.ChromeOptions()
    # op.add_argument('--headless')
    driver = webdriver.Chrome(options=op)

    product_base = 'https://www.uniqlo.com/jp/ja/products/'
    product_url = product_base + serial_number

    driver.get(product_url)

    price_element = driver.find_element(By.CLASS_NAME, "fr-ec-price-text")

    price = price_element.text
    return [price, price, price, price]


if __name__ == "__main__":
    print(crawl('467536'))