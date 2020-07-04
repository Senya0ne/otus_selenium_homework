from .MainLocators import MainLocators


class LoginLocators(MainLocators):
    EMAIL_FIELD = "input-email"
    PASSWORD_FIELD = "input-password"
    BTN_LOGIN = "input.btn.btn-primary"
    ALERT_NOT_MATCH_KEYPAIR = "alert.alert-danger.alert-dismissible"
    ALERT_SUCCESS_FORGOTTEN_PASWORD = "alert.alert-success.alert-dismissible"
    FORGOTTEN_PASSWORD = "*//a[contains(text(), 'Forgotten Password')]"
    INPUT_EMAIL_FORGOTTEN_PASSWORD = "input-email"
    BTN_CONTINUE_FORGOTTEN_PASSWORD = "input.btn.btn-primary"
    CONTENT_MY_ACCOUNT = "*//h2[contains(text(), 'My Account')]"
