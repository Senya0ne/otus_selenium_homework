from selenium.webdriver import ActionChains

from POM.locators import MainLocators
import time
from selenium.webdriver.common.by import By


def test_main_page(web_driver, base_url):
    browser = web_driver
    browser.get(base_url)
    assert browser.title == "Your Store"


def test_footer(web_driver, base_url):
    browser = web_driver
    browser.get(base_url)
    browser.find_element(By.TAG_NAME, MainLocators.FOOTER)
    assert "Information" in browser.find_element(By.XPATH, MainLocators.FOOTER_INFORMATION).text
    assert "Customer Service" in browser.find_element(By.XPATH, MainLocators.FOOTER_CUSTOMER_SERVICE).text
    assert "Extras" in browser.find_element(By.XPATH, MainLocators.FOOTER_EXTRAS).text
    assert "My Account" in browser.find_element(By.XPATH, MainLocators.FOOTER_MY_ACCOUNT).text


def test_search(web_driver, base_url):
    browser = web_driver
    browser.get(base_url)
    browser.find_element(By.CLASS_NAME, MainLocators.SEARCH_INPUT).click()
    browser.find_element(By.CLASS_NAME, MainLocators.SEARCH_INPUT).send_keys("iphone")
    browser.find_element(By.CLASS_NAME, MainLocators.SEARCH_BTN).click()
    assert "Search - iphone" in browser.find_element(By.XPATH, MainLocators.SEARCH_TITLE).text
    assert "iPhone" in browser.find_element(By.XPATH, MainLocators.PRODUCT_NAME).text


def test_add_product_to_cart(web_driver, base_url):
    browser = web_driver
    browser.get(base_url)
    assert "0 item(s) - $0.00" in browser.find_element(By.ID, MainLocators.CARD_TOTAL).text
    browser.find_elements(By.CLASS_NAME, MainLocators.BTNS_ADD_TO_CART)[0].click()
    browser.implicitly_wait(1)
    assert "1 item(s) - $602.00" in browser.find_element(By.ID, MainLocators.CARD_TOTAL).text


def test_navbar(web_driver, base_url):
    browser = web_driver
    browser.get(base_url)
    btns = browser.find_elements_by_class_name('dropdown')
    for i in range(5):
        Hover = ActionChains(browser).move_to_element(btns[i])
        Hover.click().perform()