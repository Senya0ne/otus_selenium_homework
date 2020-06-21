def test_main_page(web_driver, url):
    browser = web_driver
    browser.get(url)
    assert browser.title == "Your Store"
