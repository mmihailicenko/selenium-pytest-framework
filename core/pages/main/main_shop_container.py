from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.pages.base_page import BasePage
from core.pages.header.header_cart_popup import HeaderCartPopup


# todo: implement logging in framework and step logging to every class
class MainShopContainer(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCTS = (By.CSS_SELECTOR, ".product-small")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".name .woocommerce-loop-product__link")

    def add_to_cart(self, value: str):
        self.click_element(self.get_cart_btn_by_product(value))
        return MainShopContainer(self)

    def and_get_header_cart_popup(self) -> HeaderCartPopup:
        return HeaderCartPopup(self)

    def get_cart_btn_by_product(self, value: str) -> WebElement:
        return self.search_items_by(self.get_products(), self.PRODUCT_TITLE, value).find_element(*self.ADD_TO_CART_BTN)

    def get_products(self) -> list:
        return self.find_elements(*self.PRODUCTS)
