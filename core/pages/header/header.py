from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage
from core.pages.main.main_page import MainPage


class Header(BasePage):

    LOGO_TITLE = (By.CSS_SELECTOR, "#logo .title")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".search-field")
    SEARCH_SUBMIT_BTN = (By.CSS_SELECTOR, ".search-submit")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")

    def and_get_main_page(self) -> MainPage:
        return MainPage(self)

    def set_search(self, value: str):
        self.set_text(*self.SEARCH_FIELD, value)
        return Header(self)

    def submit_search(self):
        self.submit(*self.SEARCH_SUBMIT_BTN)
        return Header(self)
