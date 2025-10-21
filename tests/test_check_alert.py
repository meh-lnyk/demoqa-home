import pytest
from pages.alerts import Alerts

@pytest.mark.dependency(name='test_check_timer_alert_button')
def test_check_timer_alert_button(browser):
    site_obj = Alerts(browser)
    site_obj.visit()

    assert site_obj.find_elements(site_obj.timer_alert_button_locator)
