import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Параметры для тестов"""
    parser.addoption('--browser',
                     action='store',
                     default=webdriver.Chrome(),
                     help='Передайте браузер с помощью параметра --browser')


@pytest.fixture
def browser_param(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--browser')
