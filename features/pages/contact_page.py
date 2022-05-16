from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context, context.driver)

    locator = {
                'forename': (By.ID, 'forename'),
                'surname': (By.ID, 'surname'),
                'email': (By.ID, 'email'),
                'telephone': (By.ID, 'telephone'),
                'message': (By.ID, 'message'),
                'Email error': (By.ID, 'email-err'),
                'Forename error': (By.ID, 'forename-err'),
                'Message error': (By.ID, 'message-err'),
                'header': (By.ID, 'header-message'),
                'submit_button': (By.LINK_TEXT, 'Submit'),
                'back_button': (By.PARTIAL_LINK_TEXT, 'Back'),
                'submit_success_header': (By.CLASS_NAME, 'alert-success'),
                'sending_feedback_modal': (By.CLASS_NAME, 'in')
    }

    def enter_forename(self, forename):
        self._find_element(*self.locator['forename']).send_keys(forename)

    def enter_surname(self, surname):
        self._find_element(*self.locator['surname']).send_keys(surname)

    def enter_email(self, email):
        self._find_element(*self.locator['email']).send_keys(email)

    def enter_telephone(self, telephone):
        self._find_element(*self.locator['telephone']).send_keys(telephone)

    def enter_message(self, message):
        self._find_element(*self.locator['message']).send_keys(message)

    def click_submit(self):
        self._find_element(*self.locator['submit_button']).click()

    def get_error_message(self, field):
        return self._find_element(*self.locator[field]).text

    def get_header_message(self):
        return self._find_element(*self.locator['header']).text

    def get_header_successful_message(self):
        return self._find_element(*self.locator['submit_success_header']).text
        
    def check_field_error_exists(self, field):
        return self._find_elements(*self.locator[field])

    def wait_sending_feedback_to_disappear(self):
        self._wait_element_to_disappear(*self.locator['sending_feedback_modal'])

    def fill_fields(self, field, value):
        if field == 'Forename':
            self.enter_forename(value)
        elif field == 'Surname':
            self.enter_surname(value)
        elif field == 'Email':
            self.enter_email(value)
        elif field == 'Telephone':
            self.enter_telephone(value)
        elif field == 'Message':
            self.enter_message(value)
        else:
            raise NameError(f'{field} does not exist')

    