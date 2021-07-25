from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage


class MainShopContainer(BasePage):
    SHOP_CONTAINER = (By.CSS_SELECTOR, "[id=\"main\"] .shop-container")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCTS = (By.CSS_SELECTOR, ".product-small")

    def get_products(self):
        elements = self.find_elements(self.PRODUCTS)
        return elements

    def verify_book_present(self, value):
        assert self.get_products() is value, "Logo title is incorrect"
        return MainShopContainer(self)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        return MainShopContainer(self)
