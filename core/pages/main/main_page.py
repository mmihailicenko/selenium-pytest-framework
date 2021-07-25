from core.pages.base_page import BasePage
from core.pages.main.main_shop_container import MainShopContainer


class MainPage(BasePage):

    def and_get_main_shop_container(self):
        return MainShopContainer(self)
