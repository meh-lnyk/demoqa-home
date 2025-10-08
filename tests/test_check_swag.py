from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    site_obj = SwagLabs(browser)
    site_obj.visit()

    assert site_obj.exist_icon()


def test_check_login(browser):
    site_obj = SwagLabs(browser)
    site_obj.visit()

    assert site_obj.find_element('#user-name')


def test_check_password(browser):
    site_obj = SwagLabs(browser)
    site_obj.visit()

    assert site_obj.find_element('#password')
