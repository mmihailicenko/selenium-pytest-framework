from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage
from core.pages.header.header_cart_popup import HeaderCartPopup


# todo: implement logging in framework and step logging to every class
class MainShopContainer(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCTS = (By.CSS_SELECTOR, ".product-small")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".name .woocommerce-loop-product__link")
    SHOP_CONTAINER_ROOT = (By.CSS_SELECTOR, "[id='main'] .shop-container")

    def add_to_cart(self, value):
        self.click_element(self.get_cart_btn(value))
        return MainShopContainer(self)

    def get_cart_btn(self, value):
        return self.search_items_by(value, *self.PRODUCTS, *self.PRODUCT_TITLE).find_element(*self.ADD_TO_CART_BTN)

    def get_products(self):
        return self.find_elements(*self.PRODUCTS)

    def get_root_element(self):
        return self.find_element(*self.SHOP_CONTAINER_ROOT)

    def verify_book_present_by_title(self, value):
        assert self.search_items_by(value, *self.PRODUCTS, *self.PRODUCT_TITLE) \
                   .text == value, "Book %r is not found" % value
        return MainShopContainer(self)

    def and_get_header_cart_popup(self):
        return HeaderCartPopup(self)
