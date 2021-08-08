from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.pages.base_page import BasePage
from core.pages.cart.cart_page import CartPage


class HeaderCartPopup(BasePage):

    CART_LIST = (By.CSS_SELECTOR, ".cart_list")
    CART_ITEM = (By.CSS_SELECTOR, ".mini_cart_item")
    NAVIGATE_TO_CART_BTN = (By.CSS_SELECTOR, ".button.wc-forward")
    POPUP_CONTENT = (By.CSS_SELECTOR, ".mfp-content")
    REMOVE_FROM_CART_BTN = (By.CSS_SELECTOR, ".remove_from_cart_button")
    CART_POPUP_EMPTY = (By.CSS_SELECTOR, ".woocommerce-mini-cart__empty-message")

    def get_cart_popup(self) -> WebElement:
        return self.find_element(*self.POPUP_CONTENT)

    def get_cart_products(self) -> list:
        return self.find_elements(*self.CART_LIST)

    def get_cart_delete_btn(self, value: str) -> WebElement:
        return self.search_items_by(self.get_cart_products(), self.CART_ITEM, value) \
            .find_element(*self.REMOVE_FROM_CART_BTN)

    def delete_cart_item(self, value: str):
        self.click_element(self.get_cart_delete_btn(value))
        return HeaderCartPopup(self)

    def navigate_to_cart(self) -> CartPage:
        self.wait_for_element_to_be_visible(self.NAVIGATE_TO_CART_BTN)
        self.click_element(self.find_element(*self.NAVIGATE_TO_CART_BTN))
        return CartPage(self)

    def verify_cart_is_empty(self) -> bool:
        return self.is_element_present(*self.CART_POPUP_EMPTY)
