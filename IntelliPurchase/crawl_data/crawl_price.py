from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv


def crawl_tgdd(link):

    driver = webdriver.Chrome()
    driver.get(link)
    sleep(5)

    price = None

    try:
        price = driver.find_element(By.XPATH, "//p[@class='box-price-present']").text
    except:
        pass

    try:
        price = driver.find_element(By.XPATH, "//div[@class='bs_price']/strong").text
    except:
        pass

    try:
        price = driver.find_element(By.XPATH, "//div[@class='item cf-left']/b/b").text
    except:
        pass

    return price


def crawl_fpt(link):

    driver = webdriver.Chrome()
    driver.get(link)
    sleep(5)

    price = None

    try:
        price = driver.find_element(By.XPATH, "//div[@class='st-price-main']").text
    except:
        pass

    return price


def main():
    link = "https://fptshop.com.vn/dien-thoai/xiaomi-redmi-a3"
    if "thegioididong.com" in link:
        print(crawl_tgdd(link))
    elif "fptshop.com.vn" in link:
        print(crawl_fpt(link))


if __name__ == "__main__":
    main()
