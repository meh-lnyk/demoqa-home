import time
import pytest
from pages.modal_dialogs import ModalDialogs

@pytest.mark.dependency(name='test_check_modal_buttons')
def test_check_modal_buttons(browser):
    site_obj = ModalDialogs(browser)
    site_obj.visit()

    assert site_obj.find_element(site_obj.small_modal_button_locator)
    assert site_obj.find_element(site_obj.large_modal_button_locator)

@pytest.mark.dependency(depends=['test_check_modal_buttons'])
def test_modal_close(browser):
    site_obj = ModalDialogs(browser)
    site_obj.visit()

    site_obj.find_element(site_obj.small_modal_button_locator).click()
    time.sleep(1)
    assert site_obj.find_elements(site_obj.modal_content_locator)
    site_obj.find_element(site_obj.small_modal_close_button_locator).click()
    assert not site_obj.find_elements(site_obj.modal_content_locator)

    site_obj.find_element(site_obj.large_modal_button_locator).click()
    time.sleep(1)
    assert site_obj.find_elements(site_obj.modal_content_locator)
    site_obj.find_element(site_obj.large_modal_close_button_locator).click()
    assert not site_obj.find_elements(site_obj.modal_content_locator)
