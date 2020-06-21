def test_main_page(web_driver, base_url):
    browser = web_driver
    browser.get(base_url)
    assert browser.title == "Your Store"
