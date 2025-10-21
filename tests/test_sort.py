import time
from pages.webtables import Webtables

def test_sort(browser):
    site_obj = Webtables(browser)
    site_obj.visit()

    site_obj.find_element(site_obj.first_name_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.first_name_column_header_locator)

    site_obj.find_element(site_obj.last_name_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.last_name_column_header_locator)

    site_obj.find_element(site_obj.age_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.age_column_header_locator)

    site_obj.find_element(site_obj.email_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.email_column_header_locator)

    site_obj.find_element(site_obj.salary_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.salary_column_header_locator)

    site_obj.find_element(site_obj.department_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.department_column_header_locator)

    site_obj.find_element(site_obj.action_column_header_locator).click()
    time.sleep(1)
    assert site_obj.has_sort_class(site_obj.action_column_header_locator)
