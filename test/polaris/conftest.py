import pytest
from core.selenium.webdriverfactory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def each_function_setup(request):
    wdf = WebDriverFactory("chrome")
    driver = wdf.get_webdriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
