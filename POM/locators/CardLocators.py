from .MainLocators import MainLocators

class CardLocators(MainLocators):
    PRICE_TAG = "*//h2[contains(text(), '$241.99')]"
    TAX_TAG = "*//li[contains(text(), 'Ex Tax: $199.99')]"
    BTN_ADD_TO_CART = "button-cart"
    CARD_IMAGE = "thumbnail"
    CARD_ARROW_RIGHT = "mfp-arrow.mfp-arrow-right.mfp-prevent-close"
    IMAGE_COUNTER = "mfp-counter"
    IMAGE_CLOSER = "mfp-close"