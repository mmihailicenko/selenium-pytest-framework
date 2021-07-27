from core.navigation.page_component_navigation import PageComponentNavigation


class UrlNavigation:
    BASE_URL = "https://www.kniga.lv"
    LANDING_PAGE_URL = "/"
    CART_PAGE_URL = "/cart"

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open_url(self, url):
        self.get(UrlNavigation.BASE_URL + url)

    def navigate_to_landing_page(self): # todo: rename
        UrlNavigation.open_url(self, UrlNavigation.LANDING_PAGE_URL)
        return PageComponentNavigation(self)

    def navigate_to_cart_page(self):
        UrlNavigation.open_url(self, UrlNavigation.CART_PAGE_URL)
        return PageComponentNavigation(self)
