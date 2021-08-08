import pytest

from core.navigation.url_navigation import UrlNavigation


@pytest.mark.smoke
class TestCartDeleteSelectedBook:
    """Scenario: Delete Selected Book From Cart
        Steps:
        - Navigate to Polaris website
        - Search for a book and add it to cart
        - Delete selected book from the pop up cart
        - Verify pop up cart is empty
    """

    BOOK_NAME = 'По ком звонит колокол'

    def test_cart_delete_selected_book(self, each_function_setup: pytest):
        """
        Navigate to Polaris website -> Search for a book and add it to cart
        Navigate to personal cart -> Delete selected book from the pop up cart
        """
        cart_header_popup = UrlNavigation(each_function_setup).navigate_to_landing_page() \
            .and_get_header() \
            .set_search(self.BOOK_NAME) \
            .submit_search() \
            .and_get_main_page() \
            .and_get_main_shop_container() \
            .add_to_cart(self.BOOK_NAME) \
            .and_get_header_cart_popup() \
            .delete_cart_item(self.BOOK_NAME)

        """Verify cart pop up is empty"""
        assert cart_header_popup.verify_cart_is_empty() is True, "Cart pop up is not empty"
