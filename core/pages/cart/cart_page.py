from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".woocommerce .woocommerce-cart-form__cart-item")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name")
    REMOVE_BTN = (By.CSS_SELECTOR, ".remove")

    def get_cart_items(self):
        return self.find_elements(*self.CART_ITEMS)

    def get_delete_btn(self, value):
        return self.search_items_by(self.CART_ITEMS, self.PRODUCT_NAME, value).find_element(*self.REMOVE_BTN)

    def delete_cart_product(self, value):
        self.click_element(self.get_delete_btn(value))
        return CartPage(self)
