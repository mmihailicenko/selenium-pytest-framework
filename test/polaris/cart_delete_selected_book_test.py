import pytest
from core.navigation.url_navigation import UrlNavigation


@pytest.mark.smoke
class TestCartDeleteSelectedBook():
    def test_cart_delete_selected_book(self, driver):
        UrlNavigation.navigate_to_landing_page(driver) \
            .and_get_landing_page() \
            .verify_login_link()

        # link = "http://selenium1py.pythonanywhere.com/"
        # page = LandingPage(browser, link)
        # page.open()
        # # page.go_to_login_page()
        # page.verify_login_link()
