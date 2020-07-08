from POM.locators import AdminLocators
from selenium.webdriver.common.by import By

url_helper = "/admin/"
user = "user"
password = "bitnami1"
email = "user@example.com"


def test_title(browser, base_url):
    browser.get(base_url + url_helper)
    assert "Administration" in browser.title


def test_auth_success(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.ID, AdminLocators.INPUT_USER).click()
    browser.find_element(By.ID, AdminLocators.INPUT_USER).send_keys(user)
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).click()
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    assert "Dashboard" in browser.title


def test_auth_failed(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    alert = browser.find_element(By.CLASS_NAME, AdminLocators.ALERT).text
    assert_text = "No match for Username and/or Password."
    assert assert_text in alert

    browser.find_element(By.ID, AdminLocators.INPUT_PWD).click()
    browser.find_element(By.ID, AdminLocators.INPUT_PWD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    assert assert_text in alert

    browser.find_element(By.ID, AdminLocators.INPUT_USER).click()
    browser.find_element(By.ID, AdminLocators.INPUT_USER).send_keys(user)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    assert assert_text in alert


def test_forgotten_password(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.XPATH, AdminLocators.FORGOTTEN_PASSWORD).click()
    browser.find_element(By.ID, AdminLocators.EMAIL_FIELD).click()
    browser.find_element(By.ID, AdminLocators.EMAIL_FIELD).send_keys(email)
    browser.find_element(By.CSS_SELECTOR, AdminLocators.BTN_LOGIN_ADMIN).click()
    assert "An email with a confirmation link has been sent your admin email address." in browser.find_element(By.CLASS_NAME, AdminLocators.ALERT).text

