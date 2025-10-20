from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    site_obj = ModalDialogs(browser)
    site_obj.visit()

    assert len(site_obj.find_elements(site_obj.buttons_locator)) == 5


def test_navigation_modal(browser):
    site_obj = ModalDialogs(browser)
    site_obj.visit()

    site_obj.refresh()
    site_obj.find_element(site_obj.main_page_button_locator).click()
    site_obj.back()
    site_obj.set_window_size_900_by_400()
    site_obj.forward()

    assert site_obj.current_url() == 'https://demoqa.com/'
    assert site_obj.title() == 'DEMOQA'

    site_obj.set_window_size_1000_by_1000()
