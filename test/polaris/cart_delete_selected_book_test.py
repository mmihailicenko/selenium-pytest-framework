import pytest
from core.navigation.url_navigation import UrlNavigation


@pytest.mark.smoke
class TestCartDeleteSelectedBook():
    BOOK_NAME = 'По ком звонит колокол'

    # todo: add a scenario doc

    def test_cart_delete_selected_book(self, driver):
        UrlNavigation.navigate_to_landing_page(driver) \
            .and_get_header() \
            .set_search(self.BOOK_NAME) \
            .submit_search() \
            .and_get_main_page() \
            .and_get_main_shop_container() \
            .add_to_cart(self.BOOK_NAME) \
            .and_get_header_cart_popup() \
            .navigate_to_cart() \
            .delete_cart_product(self.BOOK_NAME)
        # todo: add assert no book is shown after delete
