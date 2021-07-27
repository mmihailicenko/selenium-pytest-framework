from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, how, what):
        element = self.find_element(how, what)
        element.click()

    def click_element(self, element):
        element.click()

    def find_element(self, how, what):
        try:
            element = self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def find_elements(self, how, what):
        return self.driver.find_elements(how, what)

    def is_element_present(self, how, what):
        try:
            self.find_elements(how, what)
        except NoSuchElementException:
            return False
        return True

    def set_text(self, how, what, value):
        element = self.find_element(how, what)
        element.send_keys(value)

    def submit(self, how, what):
        element = self.find_element(how, what)
        element.submit()
