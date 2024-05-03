from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def crawl_tgdd(link):
    """
    Thu thập giá của sản phẩm điện thoại di động trên thế giới di động

    Parameters:
    link (str): Đường link dẫn tới sản phẩm.

    Returns:
    price (str): Giá của sản phẩm. Nếu price là None thì sản phẩm là Hết hàng hoặc Dừng bán

    Ví dụ:
    >>> crawl_tgdd("https://www.thegioididong.com/dtdd/iphone-15-pro-max")
    29.990.000₫
    """

    # Tạo một đối tượng tùy chọn cho trình duyệt Chrome
    chrome_options = Options()
    # Thêm tùy chọn "--headless" để chạy trình duyệt ở chế độ không có giao diện người dùng,
    # nghĩa là không hiển thị cửa sổ trình duyệt lên màn hình
    chrome_options.add_argument("--headless")

    # Khởi tạo webdriver với tùy chọn trên và truy cập vào đường link sản phẩm
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    sleep(5)

    price = None

    # Kiểm tra và lấy giá của sản phẩm
    try:
        price = driver.find_element(By.XPATH, "//p[@class='box-price-present']").text
    except:
        pass

    # Kiểm tra và lấy giá của sản phẩm
    try:
        price = driver.find_element(By.XPATH, "//div[@class='bs_price']/strong").text
    except:
        pass

    # Kiểm tra và lấy giá của sản phẩm
    try:
        price = driver.find_element(By.XPATH, "//div[@class='item cf-left']/b/b").text
    except:
        pass

    # Đóng webdriver
    sleep(5)
    driver.close()

    return price


def crawl_fpt(link):
    """
    Thu thập giá của sản phẩm điện thoại di động trên fptshop

    Parameters:
    link (str): Đường link dẫn tới sản phẩm.

    Returns:
    price (str): Giá của sản phẩm. Nếu price là None thì sản phẩm là Hết hàng hoặc Dừng bán

    Ví dụ:
    >>> crawl_tgdd("https://fptshop.com.vn/dien-thoai/iphone-15-pro-max")
    29.490.000₫
    """

    # Tạo một đối tượng tùy chọn cho trình duyệt Chrome
    chrome_options = Options()
    # Thêm tùy chọn "--headless" để chạy trình duyệt ở chế độ không có giao diện người dùng,
    # nghĩa là không hiển thị cửa sổ trình duyệt lên màn hình
    chrome_options.add_argument("--headless")

    # Khởi tạo webdriver với tùy chọn trên và truy cập vào đường link sản phẩm
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    sleep(5)

    price = None

    # Kiểm tra và lấy giá của sản phẩm
    try:
        price = driver.find_element(By.XPATH, "//div[@class='st-price-main']").text
    except:
        pass

    # Đóng webdriver
    sleep(5)
    driver.close()

    return price


def main():

    link = "https://fptshop.com.vn/dien-thoai/xiaomi-redmi-a3"
    if "thegioididong.com" in link:
        print(crawl_tgdd(link))
    elif "fptshop.com.vn" in link:
        print(crawl_fpt(link))


if __name__ == "__main__":
    main()
