from POM.locators import LoginLocators
from selenium.webdriver.common.by import By

url_helper = "/index.php?route=account/login"
email = "test@test.com"
password = "test"


def test_title(browser, base_url):
    browser.get(base_url + url_helper)
    assert "Account Login" in browser.title


def test_footer(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.TAG_NAME, LoginLocators.FOOTER)
    assert "Information" in browser.find_element(By.XPATH, LoginLocators.FOOTER_INFORMATION).text
    assert "Customer Service" in browser.find_element(By.XPATH, LoginLocators.FOOTER_CUSTOMER_SERVICE).text
    assert "Extras" in browser.find_element(By.XPATH, LoginLocators.FOOTER_EXTRAS).text
    assert "My Account" in browser.find_element(By.XPATH, LoginLocators.FOOTER_MY_ACCOUNT).text


def test_auth_success(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.ID, LoginLocators.EMAIL_FIELD).click()
    browser.find_element(By.ID, LoginLocators.EMAIL_FIELD).send_keys(email)
    browser.find_element(By.ID, LoginLocators.PASSWORD_FIELD).click()
    browser.find_element(By.ID, LoginLocators.PASSWORD_FIELD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, LoginLocators.BTN_LOGIN).click()
    assert "My Account" in browser.find_element(By.XPATH, LoginLocators.CONTENT_MY_ACCOUNT).text


def test_auth_failed(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.CSS_SELECTOR, LoginLocators.BTN_LOGIN).click()
    alert = browser.find_element(By.CLASS_NAME, LoginLocators.ALERT).text
    assert_text = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
    # assert_text = "Warning: No match for E-Mail Address and/or Password."
    assert assert_text in alert

    browser.find_element(By.ID, LoginLocators.EMAIL_FIELD).click()
    browser.find_element(By.ID, LoginLocators.EMAIL_FIELD).send_keys(email)
    browser.find_element(By.CSS_SELECTOR, LoginLocators.BTN_LOGIN).click()
    assert assert_text in alert

    browser.find_element(By.ID, LoginLocators.PASSWORD_FIELD).click()
    browser.find_element(By.ID, LoginLocators.PASSWORD_FIELD).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, LoginLocators.BTN_LOGIN).click()
    assert assert_text in alert


def test_forgotten_password(browser, base_url):
    browser.get(base_url + url_helper)
    browser.find_element(By.XPATH, LoginLocators.FORGOTTEN_PASSWORD).click()
    browser.find_element(By.ID, LoginLocators.EMAIL_FIELD).click()
    browser.find_element(By.ID, LoginLocators.EMAIL_FIELD).send_keys(email)
    browser.find_element(By.CSS_SELECTOR, LoginLocators.BTN_CONTINUE_FORGOTTEN_PASSWORD).click()
    assert "An email with a confirmation link has been sent your email address." in browser.find_element(By.CLASS_NAME, LoginLocators.ALERT).text

