from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage


class LandingPage(BasePage):
    CART_LINK = (By.CSS_SELECTOR, "#cart_link")

    def go_to_cart_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, self.CART_LINK)
        login_link.click()

    def verify_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, self.CART_LINK), "Login link is not present"
