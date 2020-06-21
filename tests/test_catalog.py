import time
from POM.locators import CatalogLocators

from selenium.webdriver.common.by import By

url_helper = "/index.php?route=product/category&path=20"


def test_title(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    assert "Desktops" in browser.title


def test_quantity_desktops(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    quantity_desktops = browser.find_element_by_class_name("list-group-item.active")
    assert "Desktops (13)" in quantity_desktops.text


def test_quantity_macs(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    browser.find_element(By.LINK_TEXT, CatalogLocators.LINK_MACS).click()
    cards = browser.find_elements(By.CLASS_NAME, CatalogLocators.CARDS)
    assert 1 == len(cards)


def test_sorting_za(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    browser.find_element_by_xpath("//select[@class='form-control']/option[text()='Name (Z - A)']").click()
    products_list = browser.find_elements_by_xpath("//*[@class='product-thumb']")
    assert "Sony VAIO" in products_list[0].text