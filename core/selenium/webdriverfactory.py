from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser: str):
        self.browser = browser

    def get_webdriver(self):
        driver = None
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        return driver
