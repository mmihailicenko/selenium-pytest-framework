from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage


class MainShopContainer(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-small .box-text .name .woocommerce-loop-product__link")
    SHOP_CONTAINER_ROOT = (By.CSS_SELECTOR, "[id='main'] .shop-container")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)
        return MainShopContainer(self)

    def get_products(self):
        elements = self.find_elements(*self.PRODUCT_NAME)
        return elements

    def get_root_element(self):
        return self.find_element(*self.SHOP_CONTAINER_ROOT)

    def search_products_for(self, value):
        products_list = self.get_products()
        for item in products_list:
            if item.text == value:
                return True
            else:
                return False

    def verify_book_present(self, value):
        assert self.search_products_for(value) is True, "Book %r is not found" % value
        return MainShopContainer(self)
