from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.locators import AdminLocators
from selenium.webdriver.common.by import By

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
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    data_tab = browser.find_element(By.LINK_TEXT, AdminLocators.DATA)
    data_tab.click()
    model = browser.find_element(By.ID, AdminLocators.MODEL)
    model.click()
    model.send_keys("iPhone 20")
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()


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


def test_delete_product(browser, base_url):
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
