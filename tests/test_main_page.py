

def test_main_page(web_driver):
    browser = web_driver
    browser.get("http://localhost")
    assert browser.title == "Your Store"
    browser.quit()
