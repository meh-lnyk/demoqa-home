from pages.demoqa import DemoQa

site_url = 'https://demoqa.com/'

def test_footer_text(browser):
    site_obj = DemoQa(browser, site_url)
    site_obj.visit()

    assert site_obj.find_element('footer span').text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
