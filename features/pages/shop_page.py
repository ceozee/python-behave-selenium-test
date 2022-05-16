from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShopPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context, context.driver)

    locator = {
        'price': (By.CLASS_NAME, 'product-price'),
        'button': (By.CLASS_NAME, 'btn')
    }

    def get_product_card(self, item):
        return self._find_element(By.XPATH, f"//*[contains(text(), '{item}')]/following-sibling::p")

    def get_product_price_by_name(self, item):
        product_card = self.get_product_card(item)
        price = self._extract_element(product_card, *self.locator['price']).text
        return(price)

    def buy_products_by_name_and_quantity(self, item, quantity):
        product_card = self.get_product_card(item)
        button = self._extract_element(product_card, *self.locator['button'])
        purchase = 0
        while purchase < quantity:
             button.click()
             purchase += 1