from core.navigation.page_component_navigation import PageComponentNavigation


class UrlNavigation:
    BASE_URL = "https://www.kniga.lv"
    LANDING_PAGE_URL = "/"
    CART_PAGE_URL = "/cart"

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(UrlNavigation.BASE_URL + url)

    def navigate_to_landing_page(self):  # todo: rename
        self.open_url(self.LANDING_PAGE_URL)
        return PageComponentNavigation(self.driver)

    def navigate_to_cart_page(self):
        self.open_url(self.CART_PAGE_URL)
        return PageComponentNavigation(self)
