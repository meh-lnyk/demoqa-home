from selenium.common import NoSuchElementException
from base_page import BasePage

class SwagLabs(BasePage):
    def exist_icon(self) -> bool:
        locator = 'dev.login_logo'
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True
