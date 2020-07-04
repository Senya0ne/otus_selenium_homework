from .MainLocators import MainLocators


class LoginLocators(MainLocators):
    PASSWORD_FIELD = "input-password"
    BTN_CONTINUE_FORGOTTEN_PASSWORD = "input.btn.btn-primary"
    CONTENT_MY_ACCOUNT = "*//h2[contains(text(), 'My Account')]"
    BTN_LOGIN = "input.btn.btn-primary"