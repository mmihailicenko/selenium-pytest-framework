import pytest

from core.pages.landing.landing_page import LandingPage

@pytest.mark.smoke
class TestCartDeleteSelectedBoot():
    def cart_delete_selected_book_test(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LandingPage(browser, link)
        page.open()
        # page.go_to_login_page()
        page.verify_login_link()
