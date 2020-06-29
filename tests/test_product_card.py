from POM.locators import CardLocators
from selenium.webdriver.common.by import By

url_helper = "/index.php?route=product/product&path=57&product_id=49"


def test_title(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    assert "Samsung Galaxy Tab 10.1" in browser.title


def test_price_galaxy_tab_10_1(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    assert "$241.99" in browser.find_element(By.XPATH, CardLocators.PRICE_TAG).text


def test_taxes(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    assert "Ex Tax: $199.99" in browser.find_element(By.XPATH, CardLocators.TAX_TAG).text


def test_price_change(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    assert "0 item(s) - $0.00" in browser.find_element(By.ID, CardLocators.CARD_TOTAL).text
    browser.find_element(By.ID, CardLocators.BTN_ADD_TO_CART).click()
    assert "1 item(s) - $241.99" in browser.find_element(By.ID, CardLocators.CARD_TOTAL).text


def test_image_card(web_driver, base_url):
    browser = web_driver
    browser.get(base_url + url_helper)
    browser.find_element(By.CLASS_NAME, CardLocators.CARD_IMAGE).click()
    assert "1 of 7" in browser.find_element(By.CLASS_NAME, CardLocators.IMAGE_COUNTER).text
    browser.find_element(By.CLASS_NAME, CardLocators.CARD_ARROW_RIGHT).click()
    assert "2 of 7" in browser.find_element(By.CLASS_NAME, CardLocators.IMAGE_COUNTER).text
    browser.find_element(By.CLASS_NAME, CardLocators.IMAGE_CLOSER).click()
    assert "Samsung Galaxy Tab 10.1" in browser.title


