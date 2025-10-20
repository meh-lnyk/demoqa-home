from pages.modal_dialogs import ModalDialogs

def test_check_modal_buttons(browser):
    site_obj = ModalDialogs(browser)
    site_obj.visit()

    assert site_obj.find_element(site_obj.small_modal_button_locator)
    assert site_obj.find_element(site_obj.large_modal_button_locator)
