from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage


class MainShopContainer(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCTS = (By.CSS_SELECTOR, ".product-small")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".name .woocommerce-loop-product__link")
    SHOP_CONTAINER_ROOT = (By.CSS_SELECTOR, "[id='main'] .shop-container")

    def add_to_cart(self, value):
        self.click_element(self.get_cart_btn(value))
        return MainShopContainer(self)

    def get_cart_btn(self, value):
        return self.search_products_by_title(value).find_element(*self.ADD_TO_CART_BTN)

    def get_products(self):
        return self.find_elements(*self.PRODUCTS)

    def get_root_element(self):
        return self.find_element(*self.SHOP_CONTAINER_ROOT)

    def search_products_by_title(self, value):
        products_list = self.get_products()
        for item in products_list:
            try:
                if item.find_element(*self.PRODUCT_TITLE).text == value:
                    return item
            except Exception as e:
                print("Error: %r" % e)

    def verify_book_present_by_title(self, value):
        assert self.search_products_by_title(value).text == value, "Book %r is not found" % value
        return MainShopContainer(self)
