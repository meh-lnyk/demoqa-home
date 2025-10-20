from pages.base_page import BasePage

class ModalDialogs(BasePage):
    site_url = 'https://demoqa.com/modal-dialogs'
    def __init__(self, driver):
        super().__init__(driver, self.site_url)

    buttons_locator = '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > *'

    main_page_button_locator = '#app > header > a'
    small_modal_button_locator = '#showSmallModal'
    large_modal_button_locator = '#showLargeModal'
    modal_content_locator = 'body > div.fade.modal.show > div > div'
    modal_close_button_locator = 'body > div.fade.modal.show > div > div > div.modal-header > button'
