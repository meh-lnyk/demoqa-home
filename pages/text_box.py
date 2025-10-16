from pages.demoqa import DemoQa

class TextBox(DemoQa):
    full_name_input_locator = '#userName'
    current_address_textarea_locator = 'textarea#currentAddress'
    submit_button_locator = 'button#submit'
    full_name_field_locator = 'p#name.mb-1'
    current_address_field_locator = 'p#currentAddress.mb-1'

