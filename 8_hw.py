# pages/accordion.py
from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section1_heading = WebElement(driver, '#section1Heading')
        self.section1_content = WebElement(driver, '#section1Content > p')
        self.section2_heading = WebElement(driver, '#section2Heading')
        self.section2_content_p1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section2_content_p2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section3 = WebElement(driver, '#section3Heading')
        self.section3_content = WebElement(driver, '#section3Content > p')


# tests/test_visible_hw.py
import time
from pages.accordion import Accordion


def test_accordion_interaction(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert accordion_page.section1_content.visible()

    accordion_page.section1_heading.click()
    time.sleep(2)
    assert not accordion_page.section1_content.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert not accordion_page.section2_content_p1.visible()
    assert not accordion_page.section2_content_p2.visible()
    assert not accordion_page.section3_content.visible()
