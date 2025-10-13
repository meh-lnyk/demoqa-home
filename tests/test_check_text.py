from pages.demoqa import DemoQa

site_url = 'https://demoqa.com/'

def test_footer_text(browser):
    site_obj = DemoQa(browser, site_url)
    site_obj.visit()

    footer_text = 'footer span'
    assert site_obj.get_text(footer_text) == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'



def test_check_elements_text(browser):
    site_obj = DemoQa(browser, site_url)
    site_obj.visit()

    elements_button = site_obj.find_element('#app > div > div > div.home-body > div > div:nth-child(1)')
    elements_button.click()
    text_locator = "#app > div > div > div > div.col-12.mt-4.col-md-6"
    assert site_obj.get_text(text_locator) == 'Please select an item from left to start practice.'
