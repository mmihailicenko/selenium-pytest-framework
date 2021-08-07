from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver  # todo: chrome specific should be universal


class WebDriverFactory(object):

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver(self) -> WebDriver:
        driver = None
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        return driver
