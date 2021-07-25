from selenium.webdriver.common.by import By

from .base_page import BasePage


class LandingPage(BasePage):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, self.LOGIN_LINK)
        login_link.click()

    def verify_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, self.LOGIN_LINK), "Login link is not present"
