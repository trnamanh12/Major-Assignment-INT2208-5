import threading
from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class CrawlerThread(threading.Thread):
    """
    Một lớp đại diện cho một luồng thu thập giá sản phẩm.

    Attributes:
        link (str): Đường liên kết URL để thu thập dữ liệu.
        result_queue (Queue): Một hàng đợi để lưu trữ các kết quả thu thập.

    Methods:
        crawl_tgdd(link): Thu thập giá của sản phẩm điện thoại từ "thegioididong.com".
        crawl_fpt(link): Thu thập giá của sản phẩm điện thoại từ "fptshop.com.vn".
        crawl_link(link): Thu thập giá của sản phẩm điện thoại dựa trên liên kết được cung cấp.
        run(): Gọi phương thức crawl_link và đưa kết quả vào result_queue.
    """

    def __init__(self, link, result_queue):
        """Khởi tạo đối tượng CrawlerThread kế thừa từ threading.Thread.

        Parameters:
            link (str): Đường liên kết URL cần thu thập dữ liệu.
            result_queue (Queue): Một hàng đợi để lưu trữ các kết quả thu thập.
        """
        super().__init__()
        self.link = link
        self.result_queue = result_queue

    def crawl_tgdd(self, link):
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
        # Thêm tùy chọn "--log-level=3" để tắt thông báo lỗi của webdriver
        chrome_options.add_argument("--log-level=3")

        # Khởi tạo webdriver với tùy chọn trên và truy cập vào đường link sản phẩm
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(link)

        css_selectors = [
            "p.box-price-present",
            "div.bs_price > strong",
            "div.item.cf-left > b > b",
        ]
        # Kiểm tra tất cả các css_selector và trả về giá nếu tìm thấy
        for css_selector in css_selectors:
            try:
                price = driver.find_element(By.CSS_SELECTOR, css_selector).text
                if price != "":
                    driver.quit()
                    return price
            except:
                pass

        # Đóng webdriver
        driver.quit()
        return None

    def crawl_fpt(self, link):
        """
        Thu thập giá của sản phẩm điện thoại di động trên fptshop

        Parameters:
            link (str): Đường link dẫn tới sản phẩm.

        Returns:
            price (str): Giá của sản phẩm. Nếu price là None thì sản phẩm là Hết hàng hoặc Dừng bán

        Ví dụ:
            >>> crawl_fpt("https://fptshop.com.vn/dien-thoai/iphone-15-pro-max")
            29.490.000₫
        """
        # Tạo một đối tượng tùy chọn cho trình duyệt Chrome
        chrome_options = Options()
        # Thêm tùy chọn "--headless" để chạy trình duyệt ở chế độ không có giao diện người dùng,
        # nghĩa là không hiển thị cửa sổ trình duyệt lên màn hình
        chrome_options.add_argument("--headless")
        # Thêm tùy chọn "--log-level=3" để tắt thông báo lỗi của webdriver
        chrome_options.add_argument("--log-level=3")

        # Khởi tạo webdriver với tùy chọn trên và truy cập vào đường link sản phẩm
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(link)

        # Kiểm tra và lấy giá của sản phẩm
        try:
            price = driver.find_element(By.CSS_SELECTOR, "div.st-price-main").text
            if price != "":
                driver.quit()
                return price
        except:
            pass

        driver.quit()
        return None

    def crawl_link(self, link):
        """
        Thu thập giá của sản phẩm điện thoại di động dựa trên link sản phẩm

        Parameters:
            link (str): Đường dẫn URL của sản phẩm cần thu thập

        Returns:
            Sử dung hàm crawl_tgdd hoặc crawl_fpt để thu thập giá sản phẩm dựa trên link sản phẩm tương ứng
        """
        if "thegioididong.com" in link:
            return self.crawl_tgdd(link)
        elif "fptshop.com.vn" in link:
            return self.crawl_fpt(link)
        else:
            return "Unsupported website"

    def run(self):
        """
        Gọi hàm crawl_link và đưa kết quả vào result_queue
        """
        result = self.crawl_link(self.link)
        self.result_queue.put(result)


def main():
    # Thay đổi links để thu thập giá từ các trang web khác nhau
    links = [
        "https://fptshop.com.vn/dien-thoai/xiaomi-redmi-a3",
        "https://www.thegioididong.com/dtdd/iphone-15-pro-max-1tb",
        "https://www.thegioididong.com/dtdd/iphone-15-pro-max-512gb",
        "https://www.thegioididong.com/dtdd/iphone-15-pro-max",
    ]

    result_queue = Queue()
    threads = []

    for link in links:
        thread = CrawlerThread(link, result_queue)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Lấy kết quả từ hàng đợi và in ra màn hình (có thể thay đổi tùy mục đích sử dụng)
    while not result_queue.empty():
        result = result_queue.get()
        print(result)


if __name__ == "__main__":
    main()
