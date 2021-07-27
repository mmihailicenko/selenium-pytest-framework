from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage


class MainShopContainer(BasePage):
    SHOP_CONTAINER_ROOT = (By.CSS_SELECTOR, "[id='main'] .shop-container")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCTS = (By.CSS_SELECTOR, ".product-small .box-text .name .woocommerce-loop-product__link")

    def get_root_element(self):
        return self.find_element(*self.SHOP_CONTAINER_ROOT)

    def get_products(self):
        elements = self.find_elements(*self.PRODUCTS)
        return elements

    def verify_book_present(self, value):
        book_list = self.get_products()
        for item in book_list:
            if item.text == value:
                book = item.text
            else:
                raise Exception("Book %r is not found" % value)
        assert book == value, "Book %r is not found" % value
        return MainShopContainer(self)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        return MainShopContainer(self)
