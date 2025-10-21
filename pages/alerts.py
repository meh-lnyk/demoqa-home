from pages.base_page import BasePage

class Alerts(BasePage):
    site_url = 'https://demoqa.com/alerts'
    def __init__(self, driver):
        super().__init__(driver, self.site_url)

    timer_alert_button_locator = '#timerAlertButton'
