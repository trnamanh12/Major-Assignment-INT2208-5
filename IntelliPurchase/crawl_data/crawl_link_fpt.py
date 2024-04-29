from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv


def crawl(index):

    driver = webdriver.Chrome()
    driver.get(f"https://fptshop.com.vn/dien-thoai?sort=ban-chay-nhat&trang=4")
    sleep(5)

    try:
        name = driver.find_element(
            By.XPATH,
            "//*[@id='root']/main/div/div[3]/div[2]/div[2]/div/div[2]/div["
            + str(index)
            + "]/div[2]/h3/a",
        ).text
    except:
        pass

    try:
        driver.find_element(
            By.XPATH,
            "//*[@id='root']/main/div/div[3]/div[2]/div[2]/div/div[2]/div["
            + str(index)
            + "]",
        ).click()
        sleep(5)
    except:
        pass

    try:
        driver.find_element(
            By.XPATH,
            "//*[@id='root']/main/div/div[3]/div[2]/div[2]/div/div[2]/div["
            + str(index)
            + "]/div[1]",
        ).click()
        sleep(5)
    except:
        pass

    links = [driver.current_url]

    try:
        link_list = driver.find_elements(
            By.XPATH,
            "//div[@class='st-select']/a[@class='st-select__item js--select-item']",
        )

        for link in link_list:
            if link.get_attribute("href") not in links:
                links.append(link.get_attribute("href"))
    except:
        pass

    with open("data_tmp.csv", "a", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, links])

    sleep(5)
    driver.close()


def main():
    nums = range(1, 96)
    for i in nums:
        if i % 10 == 0:
            continue
        crawl(i)


if __name__ == "__main__":
    main()
