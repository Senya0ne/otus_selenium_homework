import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Параметры для тестов"""

    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='Передайте драйвер браузера с помощью параметра --browser, доступны safari, firefox, chrome'
                          ', например, --browser=safari')

    parser.addoption('--url',
                     action='store',
                     default='http://localhost',
                     help='Передайте url с помощью параметра --url, например, --url=https://yandex.ru')


@pytest.fixture
def url_param(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')


@pytest.fixture()
def web_driver(request):
    """
    Фикстура для инициализации драйверов
    """

    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument("headless")
    ch_options.add_argument("--kiosk")

    ff_options = webdriver.FirefoxOptions()
    ff_options.headless = True
    ff_options.add_argument("--kiosk")

    browser = request.config.getoption('--browser')

    if browser == 'firefox':
        driver = webdriver.Firefox(firefox_options=ff_options)
    elif browser == 'chrome':
        driver = webdriver.Chrome(chrome_options=ch_options)
    elif browser == 'safari':
        driver = webdriver.Safari()
        driver.maximize_window()

    driver.delete_all_cookies()

    def driver_finalizer():
        driver.quit()

    request.addfinalizer(driver_finalizer)
    return driver
