from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
            self.find_element(how, what)
        except Exception as e:
            print("Error: %r" % e)
            return False
        return True

    def set_text(self, how, what, value):
        element = self.find_element(how, what)
        element.send_keys(value)

    def search_items_by(self, where, what, value):
        elements = self.find_elements(*where)
        for item in elements:
            try:
                if item.find_element(*what).text == value:
                    return item
            except Exception as e:
                print("Error: %r" % e)

    def submit(self, how, what):
        element = self.find_element(how, what)
        element.submit()

    def wait_for_element_to_be_visible(self, locator, timeout=10, poll_frequency=0.5):
        element = None
        try:
            wait = WebDriverWait(self.driver,
                                 timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     AttributeError])
            element = wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print("Error: %r" % e)
        return element
