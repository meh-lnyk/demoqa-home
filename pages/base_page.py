from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def find_elements(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def set_window_size_900_by_400(self ):
        self.driver.set_window_size(900, 400)

    def forward(self):
        self.driver.forward()

    def current_url(self):
        return self.driver.current_url

    def title(self):
        return self.driver.title

    def set_window_size_1000_by_1000(self):
        self.driver.set_window_size(1000, 1000)

    def scroll_into_view(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)
