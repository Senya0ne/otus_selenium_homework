""" string for pylint"""
import pytest
from selenium import webdriver



def pytest_addoption(parser):
    """Параметры для запуска тестов"""

    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='Передайте драйвер браузера с помощью параметра --browser, '
                          'доступны safari, firefox, chrome'
                          ', например, --browser=safari')

    parser.addoption('--url',
                     action='store',
                     default='http://localhost',
                     help='Передайте url с помощью параметра --url,'
                          'например, --url=https://yandex.ru')


@pytest.fixture
def base_url(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')


@pytest.fixture()
def web_driver(request):
    """
    Фикстура для инициализации и передачи драйверов
    """

    browser = request.config.getoption('--browser')

    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.headless = True
        driver = webdriver.Chrome(options=options, executable_path="./drivers/chromedriver")
        driver.maximize_window()
    elif browser == 'safari':
        driver = webdriver.Safari()
        driver.maximize_window()

    def driver_finalizer():
        driver.quit()

    request.addfinalizer(driver_finalizer)
    return driver
