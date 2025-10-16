from pages.base_page import BasePage

class AutomationPracticeForm(BasePage):
    first_name_locator = 'input#firstName.mr-sm-2.form-control'
    last_name_locator = 'input#lastName.mr-sm-2.form-control'
    user_email_locator = 'input#userEmail.mr-sm-2.form-control'
    # user_email_pattern = '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    first_name_expected_placeholder = 'First Name'
    last_name_expected_placeholder = 'Last Name'
    user_email_expected_placeholder = 'name@example.com'
    form_validated_attribute = 'form#userForm.was-validated'
    submit_button_locator = 'button#submit.btn.btn-primary'
