from core.pages.landing.landing_page import LandingPage


class PageComponentNavigation:
    def __init__(self, driver):
        self.driver = driver

    def and_get_landing_page(self):
        return LandingPage(self.driver)
