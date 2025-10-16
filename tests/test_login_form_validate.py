from pages.automation_practice_form import AutomationPracticeForm

site_url = 'https://demoqa.com/automation-practice-form'

def test_login_form_validate(browser):
    site_obj = AutomationPracticeForm(browser,site_url)
    site_obj.visit()

    assert site_obj.find_element(site_obj.first_name_locator).get_attribute('placeholder') == site_obj.first_name_expected_placeholder
    assert site_obj.find_element(site_obj.last_name_locator).get_attribute('placeholder') == site_obj.last_name_expected_placeholder
    assert site_obj.find_element(site_obj.user_email_locator).get_attribute('placeholder') == site_obj.user_email_expected_placeholder

    assert site_obj.find_element(f'{site_obj.user_email_locator}[pattern]')

    site_obj.scroll_into_view(site_obj.find_element(site_obj.submit_button_locator))
    site_obj.find_element(site_obj.submit_button_locator).click()
    assert site_obj.find_element(site_obj.form_validated_attribute)
