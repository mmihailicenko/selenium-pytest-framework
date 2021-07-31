from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage
from core.pages.cart.cart_page import CartPage


class HeaderCartPopup(BasePage):
    POPUP_CONTENT = (By.CSS_SELECTOR, ".mfp-content")
    NAVIGATE_TO_CART_BTN = (By.CSS_SELECTOR, ".button.wc-forward")

    def get_cart_popup(self):
        return self.find_element(*self.POPUP_CONTENT)

    def navigate_to_cart(self):
        self.wait_for_element_to_be_visible(self.NAVIGATE_TO_CART_BTN)
        self.click_element(self.find_element(*self.NAVIGATE_TO_CART_BTN))
        return CartPage(self)
