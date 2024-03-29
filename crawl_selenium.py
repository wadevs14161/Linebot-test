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


    # search.clear()   # 清除框框（以免有預設值）
    # search.send_keys(467536)  # 輸入要搜尋的關鍵字（這邊放商品代號）
    # search_icon.click()  # 點擊送出

    price = price_element.text
    return price


if __name__ == "__main__":
    price = crawl('467536')
    print(price)