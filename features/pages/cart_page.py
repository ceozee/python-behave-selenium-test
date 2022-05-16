from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context, context.driver)

    locator = {
        'name': (By.CSS_SELECTOR, 'td:nth-child(1)'),
        'price': (By.CSS_SELECTOR, 'td:nth-child(2)'),
        'quantity': (By.CSS_SELECTOR, 'td:nth-child(3)>input'),
        'subtotal': (By.CSS_SELECTOR, 'td:nth-child(4)'),
        'total': (By.CLASS_NAME, 'total'),
        'checkout_button': (By.LINK_TEXT, 'Check Out'),
        'empty_cart_button': (By.LINK_TEXT, 'Empty Cart')            
    }


    def get_all_purchases(self):
        rows = self._find_elements(By.CLASS_NAME, 'cart-item')
        purchase_id = 0
        purchase_list_dict = {}
        for row in rows:
            item = rows[purchase_id].find_element(*self.locator['name']).text
            price = rows[purchase_id].find_element(*self.locator['price']).text
            quantity = rows[purchase_id].find_element(*self.locator['quantity']).get_attribute('value')
            subtotal = rows[purchase_id].find_element(*self.locator['subtotal']).text

            purchase_list_dict[item] =  {
                    'name': item,
                    'price': price,
                    'quantity': quantity,
                    'subtotal': subtotal
                }
            
            purchase_id += 1
        return purchase_list_dict

    def get_total(self):
        return (self._find_element(*self.locator['total']).text)