from .MainLocators import MainLocators


class AdminLocators(MainLocators):
    INPUT_USER = "input-username"
    INPUT_PWD = "input-password"
    BTN_LOGIN_ADMIN = "button.btn.btn-primary"
    BTN_LOGOUT = ".fa-sign-out"
    CATALOG = "parent.collapsed"
    PRODUCTS = "Products"
    ADD_PRODUCT_BTN = "a.btn.btn-primary"
    ADD_NAME_FOR_PRODUCT = "input-name1"
    ADD_METATAGS_FOR_PRODUCT = "input-meta-title1"
    DATA = "Data"
    MODEL = "input-model"
    TABLE_PRODUCTS = "*//tr"
    NAME_PRODUCTS_IN_TABLE = "td.text-left"
    PRODUCT_FOR_DELETE = "*//input[@value='42']"
    BTN_DELETE = "*//button[@data-original-title='Delete']"

