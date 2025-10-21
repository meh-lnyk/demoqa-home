import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.alerts import Alerts

@pytest.mark.dependency(name='test_check_timer_alert_button')
def test_check_timer_alert_button(browser):
    site_obj = Alerts(browser)
    site_obj.visit()

    assert site_obj.find_elements(site_obj.timer_alert_button_locator)

@pytest.mark.dependency(depends=['test_check_timer_alert_button'])
def test_alert_showup_time(browser):
    site_obj = Alerts(browser)
    site_obj.visit()

    site_obj.find_element(site_obj.timer_alert_button_locator).click()
    WebDriverWait(browser, 5).until(EC.alert_is_present())
    assert EC.alert_is_present()
