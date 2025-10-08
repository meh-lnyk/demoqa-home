from selenium.common import NoSuchElementException
from pages.base_page import BasePage

class SwagLabs(BasePage):
    def exist_icon(self) -> bool:
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True
