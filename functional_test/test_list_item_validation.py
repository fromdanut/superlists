from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit an empty
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        # The browser intercepts the request, and doesn't load the list page.
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))
        # She types some text for the new item, the error disappears.
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))

        # She can submit.
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # She decides to add a second empty submit, she receives same warning.
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # She can correct it by filling text in.
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
