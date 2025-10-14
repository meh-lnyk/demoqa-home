from pages.base_page import BasePage

class Accordian(BasePage):
    content_locator = '#section1Content > p'
    heading_locator = '#section1Heading'

    section_2_child_1_locator = '#section2Content > p:nth-child(1)'
    section_2_child_2_locator = '#section2Content > p:nth-child(2)'
    section_3_locator = '#section3Content > p'
