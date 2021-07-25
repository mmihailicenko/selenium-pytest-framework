import pytest

from core.pages.landing.landing_page import LandingPage

@pytest.mark.smoke
class TestCartDeleteSelectedBoot():
    def test_cart_delete_selected_book(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LandingPage(browser, link)
        page.open()
        # page.go_to_login_page()
        page.verify_login_link()
