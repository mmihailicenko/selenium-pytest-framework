from core.pages.header.header import Header


class PageComponentNavigation:
    def __init__(self, driver):
        self.driver = driver

    def and_get_header(self):
        return Header(self.driver)
