from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv


def crawl_comments(index_of_products):

    check = True

    with open("comments.csv", "a", newline="", encoding="utf-8-sig") as csvfile:

        writer = csv.writer(csvfile)
        driver = webdriver.Chrome()  # Open Chrome webdriver
        driver.get("https://www.thegioididong.com/dtdd")  # Open the web
        sleep(3)

        # Click on the product
        driver.find_element(
            By.XPATH,
            "//*[@id='categoryPage']/div[3]/ul/li[" + str(index_of_products) + "]",
        ).click()
        sleep(3)

        try:
            # Click to see others comments
            driver.find_element(
                By.XPATH, "//a[@class='c-btn-rate btn-view-all']"
            ).click()
            sleep(3)
        except:
            check = False
            pass

        try:
            # Crawl comments and its star
            comments = driver.find_element(
                By.XPATH, "//div[@class='rt-list']"
            ).find_elements(By.CLASS_NAME, "cmt-txt")
            comments_stars = driver.find_element(
                By.XPATH, "//div[@class='rt-list']"
            ).find_elements(By.CLASS_NAME, "cmt-top-star")
            for i in range(len(comments)):
                txt = comments[i].text
                n_stars = len(
                    comments_stars[i].find_elements(By.CLASS_NAME, "iconcmt-starbuy")
                )
                if txt != "" or txt.strip() or (len(txt) >= 75 and len(txt) <= 300):
                    writer.writerow([txt, n_stars, ""])
        except:
            check = False
            pass

        if check == True:
            for k in range(1, 51):
                # Click on the next page button
                try:
                    driver.find_element(
                        By.XPATH, "//a[@title='trang " + str(k + 1) + "']"
                    ).click()
                    sleep(3)
                except:
                    break

                try:
                    # Crawl comments and its star
                    comments = driver.find_element(
                        By.XPATH, "//div[@class='rt-list']"
                    ).find_elements(By.CLASS_NAME, "cmt-txt")
                    comments_stars = driver.find_element(
                        By.XPATH, "//div[@class='rt-list']"
                    ).find_elements(By.CLASS_NAME, "cmt-top-star")
                    for i in range(len(comments)):
                        txt = comments[i].text
                        n_stars = len(
                            comments_stars[i].find_elements(
                                By.CLASS_NAME, "iconcmt-starbuy"
                            )
                        )
                        if (
                            txt != ""
                            or txt.strip()
                            or (len(txt) >= 75 and len(txt) <= 300)
                        ):
                            writer.writerow([txt, n_stars, ""])
                except:
                    pass

        check = True
        sleep(3)
        driver.close()  # Close the driver


def main():
    crawl_comments(1)


if __name__ == "__main__":
    main()
