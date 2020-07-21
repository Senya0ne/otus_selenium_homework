from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.locators import AdminLocators
from selenium.webdriver.common.by import By
import time

url_helper = "/admin/"
user = "user"
password = "bitnami1"
email = "user@example.com"


def test_add_product(browser, base_url):
    browser.get(base_url + url_helper)
    wait = WebDriverWait(browser, 3)
    browser.find_element(By.ID, AdminLocators.INPUT_USER).click()
    browser.find_element(By.ID, AdminLocators.INPUT_USER).send_keys(user)
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).click()
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    wait.until(EC.title_is("Dashboard"))
    browser.find_element(By.CLASS_NAME, AdminLocators.CATALOG).click()
    browser.find_element(By.LINK_TEXT, AdminLocators.PRODUCTS).click()
    browser.find_element(By.CSS_SELECTOR, AdminLocators.ADD_PRODUCT_BTN).click()
    product_name = browser.find_element(By.ID, AdminLocators.ADD_NAME_FOR_PRODUCT)
    product_name.click()
    product_name.send_keys("iPhone 20")
    meta_tags = browser.find_element(By.ID, AdminLocators.ADD_METATAGS_FOR_PRODUCT)
    meta_tags.click()
    meta_tags.send_keys("iPhone, Mobile")
    data_tab = browser.find_element(By.LINK_TEXT, AdminLocators.DATA)
    data_tab.click()
    model = browser.find_element(By.ID, AdminLocators.MODEL)
    model.click()
    model.send_keys("iPhone 20")
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_SAVE).click()
    assert "Success: You have modified products!" in browser.find_element(By.CLASS_NAME, AdminLocators.ALERT).text


def test_edit_product(browser, base_url):
    browser.get(base_url + url_helper)
    wait = WebDriverWait(browser, 3)
    browser.find_element(By.ID, AdminLocators.INPUT_USER).click()
    browser.find_element(By.ID, AdminLocators.INPUT_USER).send_keys(user)
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).click()
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    wait.until(EC.title_is("Dashboard"))
    browser.find_element(By.CLASS_NAME, AdminLocators.CATALOG).click()
    browser.find_element(By.LINK_TEXT, AdminLocators.PRODUCTS).click()
    table_products = browser.find_elements(By.XPATH, AdminLocators.TABLE_PRODUCTS)
    length_table_products = len(table_products)
    assert length_table_products > 1
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_EDIT).click()
    product_name = browser.find_element(By.ID, AdminLocators.ADD_NAME_FOR_PRODUCT)
    product_name.click()
    product_name.clear()
    product_name.send_keys("AFTER_EDIT")
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_SAVE).click()
    assert "Success: You have modified products!" in browser.find_element(By.CLASS_NAME, AdminLocators.ALERT).text


def test_delete_product(browser, base_url):
    browser.get(base_url + url_helper)
    wait = WebDriverWait(browser, 5)
    browser.find_element(By.ID, AdminLocators.INPUT_USER).click()
    browser.find_element(By.ID, AdminLocators.INPUT_USER).send_keys(user)
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).click()
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    wait.until(EC.title_is("Dashboard"))
    browser.find_element(By.CLASS_NAME, AdminLocators.CATALOG).click()
    browser.find_element(By.LINK_TEXT, AdminLocators.PRODUCTS).click()
    table_products = browser.find_elements(By.XPATH, AdminLocators.TABLE_PRODUCTS)
    length_table_products = len(table_products)
    assert length_table_products > 1
    browser.find_element(By.XPATH, AdminLocators.ID_PRODUCT_FOR_INTERACTIONS).click()
    browser.find_element(By.XPATH, AdminLocators.BTN_DELETE).click()
    alert_obj = browser.switch_to.alert
    alert_obj.accept()
    browser.implicitly_wait(5)
    alert = browser.find_element(By.CLASS_NAME, AdminLocators.ALERT)
    assert alert.is_displayed()


