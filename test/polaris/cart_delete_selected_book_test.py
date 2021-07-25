from core.pages.landing_page import LandingPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LandingPage(browser, link)
    page.open()
    # page.go_to_login_page()
    page.verify_login_link()
