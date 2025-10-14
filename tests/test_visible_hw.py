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


def test_visible_accordion_default(browser):
    site_obj = Accordian(browser, site_url)
    site_obj.visit()

    assert not site_obj.find_element(site_obj.section_2_child_1_locator).is_displayed()
    assert not site_obj.find_element(site_obj.section_2_child_2_locator).is_displayed()
    assert not site_obj.find_element(site_obj.section_3_locator).is_displayed()
