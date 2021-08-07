from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common import by
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, how: by, what: str):
        element = self.find_element(how, what)
        element.click()

    def click_element(self, element):  # todo: refactor, this works, but looks as not intended
        element.click()

    def find_element(self, how: by, what: str) -> WebElement:
        element = self.driver.find_element(how, what)
        return element

    def find_elements(self, how: by, what: str):
        return self.driver.find_elements(how, what)

    def set_text(self, how: by, what: str, value: str):
        element = self.find_element(how, what)
        element.send_keys(value)

    def search_items_by(self, where: tuple, what: tuple, value: str) -> WebElement:
        elements = self.find_elements(*where)
        for item in elements:
            if item.find_element(*what).text == value:
                return item

    def submit(self, how: by, what: str):
        element = self.find_element(how, what)
        element.submit()

    def wait_for_element_to_be_visible(self, locator: tuple, timeout=10, poll_frequency=0.5) -> WebElement:
        wait = WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                 AttributeError])
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
