from selenium.common import NoSuchElementException
from pages.base_page import BasePage

class DemoQa(BasePage):
    def get_text(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return str(self.find_element(locator).text)
