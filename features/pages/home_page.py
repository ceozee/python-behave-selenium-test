from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context, context.driver)

    locator = {
        'Start Shopping': (By.PARTIAL_LINK_TEXT, 'Start Shopping')
    }

    def click_start_shopping(self):
        self._find_element(*self.locator['Start Shopping']).click()