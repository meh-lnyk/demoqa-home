from pages.swag_labs import SwagLabs

def test_check_swag(browser):
    site_obj = SwagLabs(browser)
    site_obj.visit()

    assert site_obj.exist_icon()
