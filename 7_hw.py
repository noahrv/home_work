# файл conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



# файл base_page.py
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com'

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def visit(self):
        return self.driver.get(self.base_url)

    def get_text(self):
        return str(self.find_element().text)



# файл test_check_text.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

def test_footer_text(browser):
    page = BasePage(browser)
    page.visit()
    footer = browser.find_element(By.CSS_SELECTOR, 'footer span')
    assert footer.text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_center_text_on_elements_page(browser):
    page = BasePage(browser)
    page.visit()
    browser.find_element(By.CSS_SELECTOR, 'div.card').click()
    center_text = browser.find_element(By.CSS_SELECTOR, 'div.col-12.mt-4.col-md-6').text
    assert center_text == 'Please select an item from left to start practice.'
