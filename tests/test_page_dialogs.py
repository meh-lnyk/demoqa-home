from pages.modal_dialogs import ModalDialogs

site_url = 'https://demoqa.com/modal-dialogs'

def test_modal_elements(browser):
    site_obj = ModalDialogs(browser, site_url)
    site_obj.visit()

    assert len(site_obj.find_elements(site_obj.buttons_locator)) == 5
