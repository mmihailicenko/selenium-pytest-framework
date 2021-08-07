from core.pages.base_page import BasePage
from core.pages.header.header_cart_popup import HeaderCartPopup
from core.pages.main.main_shop_container import MainShopContainer


class MainPage(BasePage):

    def and_get_main_shop_container(self) -> MainShopContainer:
        return MainShopContainer(self)

    def and_get_header_cart_popup(self) -> HeaderCartPopup:
        return HeaderCartPopup(self)
