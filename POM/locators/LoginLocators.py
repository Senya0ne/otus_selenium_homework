from .MainLocators import MainLocators


class LoginLocators(MainLocators):
    EMAIL_FIELD = "input-email"
    PASSWORD_FIELD = "input-password"
    BTN_LOGIN = "input.btn.btn-primary"
    ALERT_NOT_MATCH_KEYPAIR = "alert.alert-danger.alert-dismissible"
    FORGOTTEN_PASSWORD = "*//[contains(text(), 'Forgotten Password')]"
    CONTENT_MY_ACCOUNT = "*//h2[contains(text(), 'My Account')]"