from POM.locators import CatalogLocators

from selenium.webdriver.common.by import By

url_helper = "/index.php?route=product/category&path=20"


def test_title(browser, base_url):
    browser.get(base_url + url_helper)
    assert "Desktops" in browser.title


def test_quantity_desktops(browser, base_url):
    browser.get(base_url + url_helper)
    quantity_desktops = browser.find_element_by_class_name("list-group-item.active")
    assert "Desktops (13)" in quantity_desktops.text


def test_quantity_macs(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.LINK_TEXT, CatalogLocators.LINK_MACS).click()
    cards = browser.find_elements(By.CLASS_NAME, CatalogLocators.CARDS)
    assert 1 == len(cards)


def test_sorting_za(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element_by_xpath("//select[@class='form-control']/option[text()='Name (Z - A)']").click()
    products_list = browser.find_elements_by_xpath("//*[@class='product-thumb']")
    assert "Sony VAIO" in products_list[0].text


def test_sorting_default(browser, base_url):
    browser.get(base_url + url_helper)
    products_list = browser.find_elements_by_xpath("//*[@class='product-thumb']")
    assert "Apple Cinema 30" in products_list[0].text
