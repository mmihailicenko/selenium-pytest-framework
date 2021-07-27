import pytest
from core.navigation.url_navigation import UrlNavigation


@pytest.mark.smoke
class TestCartDeleteSelectedBook():
    LOGO_TITLE = 'Книжный интернет-магазин Kniga.lv Polaris - Русские книги в Латвии и Европе'
    BOOK_NAME = 'По ком звонит колокол'

    def test_cart_delete_selected_book(self, driver):
        UrlNavigation.navigate_to_landing_page(driver) \
            .and_get_header() \
            .set_search(self.BOOK_NAME) \
            .submit_search() \
            .and_get_main_page() \
            .and_get_main_shop_container() \
            .add_to_cart(self.BOOK_NAME)
