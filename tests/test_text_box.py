import time
from pages.text_box import TextBox

site_url = 'https://demoqa.com/text-box'

def test_text_box(browser):
    site_obj = TextBox(browser, site_url)
    site_obj.visit()

    full_name = 'Hello'
    current_address = 'World'

    site_obj.find_element(site_obj.full_name_input_locator).send_keys(full_name)
    time.sleep(1)
    site_obj.find_element(site_obj.current_address_textarea_locator).send_keys(current_address)
    time.sleep(1)
    site_obj.scroll_into_view(site_obj.find_element(site_obj.submit_button_locator))
    time.sleep(1)
    site_obj.find_element(site_obj.submit_button_locator).click()
    time.sleep(5)

    assert site_obj.find_element(site_obj.full_name_field_locator).text == f'Name:{full_name}'
    assert site_obj.find_element(site_obj.current_address_field_locator).text == f'Current Address :{current_address}'
