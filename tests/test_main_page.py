def test_main_page(web_driver, url_param):
    browser = web_driver
    browser.get(url_param)
    assert browser.title == "Your Store"
