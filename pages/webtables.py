from pages.base_page import BasePage

class Webtables(BasePage):
    site_url = 'https://demoqa.com/webtables'
    def __init__(self, driver):
        super().__init__(driver, self.site_url)

    add_button_locator = '#addNewRecordButton'
    form_modal_locator = 'body > div.fade.modal.show > div > div'
    user_form_locator = '#userForm'
    submit_form_button_locator = '#submit'

    form_first_name_locator = '#firstName'
    form_last_name_locator = '#lastName'
    form_email_locator = '#userEmail'
    form_age_locator = '#age'
    form_salary_locator = '#salary'
    form_department_locator = '#department'

    first_name_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)'
    last_name_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)'
    age_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(3)'
    email_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)'
    salary_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(5)'
    department_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)'

    edit_4th_record_button_locator = '#edit-record-4 > svg'
    delete_4th_record_button_locator = '#delete-record-4 > svg'

    total_form_pages_number_locator = '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span'
