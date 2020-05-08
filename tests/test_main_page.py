

def test_main_page(browser_param):
    browser = browser_param
    browser.get("http://localhost")
    page_title = browser.title
    assert page_title == "Your Store"
    browser.quit()
