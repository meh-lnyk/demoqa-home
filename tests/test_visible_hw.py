import time
from pages.accordian import Accordian

site_url = 'https://demoqa.com/accordian'

def test_visible_accordion(browser):
    site_obj = Accordian(browser, site_url)
    site_obj.visit()

    assert site_obj.find_element(site_obj.content_locator).is_displayed()

    site_obj.find_element(site_obj.heading_locator).click()
    time.sleep(2)

    assert not site_obj.find_element(site_obj.content_locator).is_displayed()
