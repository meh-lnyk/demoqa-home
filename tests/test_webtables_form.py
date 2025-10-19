import time

from pages.webtables import Webtables

def test_webtables_form(browser):
    site_obj = Webtables(browser)
    site_obj.visit()

    assert site_obj.find_element(site_obj.add_button_locator)

    site_obj.find_element(site_obj.add_button_locator).click()
    time.sleep(1)
    assert site_obj.find_element(site_obj.form_modal_locator)

    site_obj.find_element(site_obj.submit_form_button_locator).click()
    time.sleep(1)
    assert site_obj.find_element(site_obj.user_form_locator).get_attribute('class') == 'was-validated'

    example_person = {
        "first_name": "Hello",
        "last_name": "World",
        "email": "hello@world.com",
        "age": "30",
        "salary": "10000",
        "department": "Hello World"
    }

    site_obj.find_element(site_obj.form_first_name_locator).click()
    time.sleep(1)
    site_obj.find_element(site_obj.form_first_name_locator).send_keys(example_person['first_name'])
    time.sleep(1)
    site_obj.find_element(site_obj.form_last_name_locator).click()
    time.sleep(1)
    site_obj.find_element(site_obj.form_last_name_locator).send_keys(example_person['last_name'])
    time.sleep(1)
    site_obj.find_element(site_obj.form_email_locator).click()
    time.sleep(1)
    site_obj.find_element(site_obj.form_email_locator).send_keys(example_person['email'])
    time.sleep(1)
    site_obj.find_element(site_obj.form_age_locator).click()
    time.sleep(1)
    site_obj.find_element(site_obj.form_age_locator).send_keys(example_person['age'])
    time.sleep(1)
    site_obj.find_element(site_obj.form_salary_locator).click()
    time.sleep(1)
    site_obj.find_element(site_obj.form_salary_locator).send_keys(example_person['salary'])
    time.sleep(1)
    site_obj.find_element(site_obj.form_department_locator).click()
    time.sleep(1)
    site_obj.find_element(site_obj.form_department_locator).send_keys(example_person['department'])
    time.sleep(1)
    site_obj.find_element(site_obj.submit_form_button_locator).click()
    time.sleep(1)

    assert not site_obj.find_elements(site_obj.form_modal_locator)
    assert site_obj.find_element(site_obj.first_name_locator).text == example_person['first_name']
    assert site_obj.find_element(site_obj.last_name_locator).text == example_person['last_name']
    assert site_obj.find_element(site_obj.email_locator).text == example_person['email']
    assert site_obj.find_element(site_obj.age_locator).text == example_person['age']
    assert site_obj.find_element(site_obj.salary_locator).text == example_person['salary']
    assert site_obj.find_element(site_obj.department_locator).text == example_person['department']
