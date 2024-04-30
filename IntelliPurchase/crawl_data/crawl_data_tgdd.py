from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
import webcolors
import re


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def extract_text1(input_string):
    if "</a>" in input_string:
        start_index = input_string.find(">") + 1
        start_index = input_string.find(">", start_index) + 1
        end_index = input_string.find("<")
        end_index = input_string.find("<", end_index + 1)
        end_index = input_string.find("<", end_index + 1)
        text = input_string[start_index:end_index].strip()
    else:
        start_index = input_string.find(">") + 1
        end_index = input_string.find("<")
        end_index = input_string.find("<", end_index + 1)
        text = input_string[start_index:end_index].strip()
    return text


def extract_text2(input_string):
    if 'class="circle"' in input_string:
        end_tags_indices = []
        start_index = 0
        while True:
            start_index = input_string.find("</p>", start_index)
            if start_index == -1:
                break
            end_tags_indices.append(start_index)
            start_index += len("</p>")
        texts = ""
        for end_index in end_tags_indices:
            start_index = input_string.rfind('<p class="circle">', 0, end_index)
            text = input_string[start_index + 18 : end_index]
            if "</a>" in text:
                start_index_text = text.find(">") + 1
                end_index_text = text.find("<")
                end_index_text = text.find("<", end_index_text + 1)
                text = text[start_index_text:end_index_text].strip()
            texts += text.strip() + "\n"
        texts = texts.rstrip("\n")
        return texts
    elif 'class="comma"' in input_string:
        end_tags_indices = []
        start_index = 0
        while True:
            start_index = input_string.find("</a>", start_index)
            if start_index == -1:
                break
            end_tags_indices.append(start_index)
            start_index += len("</a>")
        texts = ""
        for end_index in end_tags_indices:
            start_index = input_string.rfind(">", 0, end_index)
            text = input_string[start_index + 1 : end_index]
            texts += text.strip() + ", "
        texts = texts.rstrip(", ")
        return texts
    else:
        start_index = input_string.find(">") + 1
        start_index = input_string.find(">", start_index) + 1
        end_index = input_string.find("<")
        end_index = input_string.find("<", end_index + 1)
        end_index = input_string.find("<", end_index + 1)
        text = input_string[start_index:end_index].strip()
        return text


def crawl(index):

    driver = webdriver.Chrome()
    driver.get("https://www.thegioididong.com/dtdd#c=42&o=17&pi=5")
    sleep(5)

    try:
        name = driver.find_element(
            By.XPATH, "//*[@id='categoryPage']/div[3]/ul/li[" + str(index) + "]/a[1]/h3"
        ).text

        image = driver.find_element(
            By.XPATH,
            "//*[@id='categoryPage']/div[3]/ul/li[" + str(index) + "]/a[1]/div[2]/img",
        ).get_attribute("src")

        driver.find_element(
            By.XPATH, "//*[@id='categoryPage']/div[3]/ul/li[" + str(index) + "]"
        ).click()
        sleep(5)
    except:
        return

    storages = []
    colors = []
    links = []

    try:
        storage = driver.find_element(
            By.XPATH,
            "//div[@class='box03 group desk']/a[@class='box03__item item act']",
        ).text

        storages.append(storage)

        storage_list = driver.find_elements(
            By.XPATH, "//div[@class='box03 group desk']/a[@class='box03__item item ']"
        )

        for storage in storage_list:
            if storage.text != "" and storage not in storages:
                storages.append(storage.text)

    except:
        pass

    if len(storages) == 0:
        try:
            storage_list = driver.find_elements(
                By.XPATH, "//div[@class='tab']/a[@class]"
            )

            for storage in storage_list:
                if storage.text != "" and storage not in storages:
                    storages.append(storage.text)

        except:
            pass

    try:
        color = driver.find_element(
            By.XPATH,
            "//div[@class='box03 color group desk']/a[@class='box03__item item act']",
        ).text

        colors.append(color)

        color_list = driver.find_elements(
            By.XPATH,
            "//div[@class='box03 color group desk']/a[@class='box03__item item ']",
        )

        for color in color_list:
            if color.text != "" and color not in colors:
                colors.append(color.text)

    except:
        pass

    if len(colors) == 0:
        try:
            color_list = driver.find_elements(
                By.XPATH,
                "//div[@class='p-color']/a[@class]",
            )

            for color in color_list:
                color = color.get_attribute("style")
                color = re.search(r"rgb\((\d+), (\d+), (\d+)\)", color)
                if color:
                    rgb = tuple(map(int, color.groups()))
                    actual_name, closest_name = get_colour_name(rgb)
                    if actual_name != None:
                        color_name = actual_name
                    else:
                        color_name = closest_name
                    if color_name not in colors:
                        colors.append(color_name)

        except:
            pass

    try:
        link_list = driver.find_elements(By.XPATH, "//div[@class='tab']/a[@class]")

        for link in link_list:
            if link.get_attribute("href") not in links:
                links.append(link.get_attribute("href"))

    except:
        pass

    if len(links) == 0:
        try:
            links.append(driver.current_url.split("?")[0])
            link_list = driver.find_elements(
                By.XPATH,
                "//div[@class='box03 group desk']/a[@class='box03__item item ']",
            )

            for link in link_list:
                link = link.get_attribute("href")
                links.append(link.split("?")[0])

        except:
            pass

    details = [name, image, links, colors, storages]

    try:
        driver.find_element(
            By.XPATH, "//span[@class='btn-detail btn-short-spec ']"
        ).click()
        sleep(5)

        param_list = ["29", "1841", "2701", "2121", "22", "24", "2122", "19", "28"]
        for param in param_list:
            try:
                elements_left = driver.find_elements(
                    By.XPATH,
                    "//ul[@class='ulist ']/li[@data-group-id='"
                    + param
                    + "']/div[@class='ctLeft']",
                )
                elements_right = driver.find_elements(
                    By.XPATH,
                    "//ul[@class='ulist ']/li[@data-group-id='"
                    + param
                    + "']/div[@class='ctRight']",
                )
                data_dict = {
                    left.text: right.text
                    for left, right in zip(elements_left, elements_right)
                }
                details.append(data_dict.copy())
            except:
                details.append({})
    except:
        pass

    try:
        driver.find_element(
            By.XPATH, "//span[@class='btn-detail btn-short-spec not-have-instruction']"
        ).click()
        sleep(5)

        param_list = ["29", "1841", "2701", "2121", "22", "24", "2122", "19", "28"]
        for param in param_list:
            elements_left = driver.find_elements(
                By.XPATH,
                "//ul[@class='ulist ']/li[@data-group-id='"
                + param
                + "']/div[@class='ctLeft']",
            )
            elements_right = driver.find_elements(
                By.XPATH,
                "//ul[@class='ulist ']/li[@data-group-id='"
                + param
                + "']/div[@class='ctRight']",
            )
            data_dict = {
                left.text: right.text
                for left, right in zip(elements_left, elements_right)
            }
            details.append(data_dict.copy())
    except:
        pass

    try:
        driver.find_element(By.XPATH, "//a[@class='viewmore']").click()
        sleep(5)

        elements = driver.find_elements(By.XPATH, "//ul[@class='parameterfull']/li")

        data_dict = {}
        for idx, element in enumerate(elements):
            if idx == 0:
                continue
            attribute = element.get_attribute("class")
            if attribute != "":
                left = driver.find_element(
                    By.XPATH,
                    f"//ul[@class='parameterfull']/li[@class='{attribute}']/span",
                )
                right = driver.find_element(
                    By.XPATH,
                    f"//ul[@class='parameterfull']/li[@class='{attribute}']/div",
                )
                left_text = extract_text1(left.get_attribute("outerHTML"))
                right_text = extract_text2(right.get_attribute("outerHTML"))
                data_dict[left_text] = right_text
            else:
                details.append(data_dict.copy())
                data_dict.clear()
        details.append(data_dict.copy())

    except:
        pass

    with open("data_tmp.csv", "a", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(details)

    sleep(5)
    driver.close()


def main():
    nums = [1]
    for i in nums:
        crawl(i)


if __name__ == "__main__":
    main()
