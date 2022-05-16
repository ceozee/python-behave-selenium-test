from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, context, driver):
        self.driver = driver
        self.base_url = context.url
        self.timeout = 30

    locator = {
        'Contact': (By.ID, 'nav-contact'),
        'Cart': (By.ID, 'nav-cart'),
        'Shop': (By.ID, 'nav-shop')
    }

    def _find_element(self, *locator):
        return self.driver.find_element(*locator)

    def _find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def _visit(self, url):
        self.driver.get(url)

    def _click(self, *locator):
        self._find_element(*locator).click()

    def _wait_element_to_disappear(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((by, value)))

    def _wait_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((by, value)))

    def _wait_clickable_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, value)))

    def click_contact_page(self):
        self._find_element(*BasePage.locator['Contact']).click()

    def click_cart_page(self):
        self._find_element(*BasePage.locator['Cart']).click()

    def click_shop_page(self):
        self._find_element(*BasePage.locator['Shop']).click()

    def visit_home_page(self):
        self._visit(self.base_url)

    def _extract_element(self, element, by, value):
        return element.find_element(by, value)


