from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit an empty
        # The home page refreshes, and there is an error message.
        # She tries again with some text, it works.
        # She decides to add a second empty submit, she receives a similir
        # warning on the list page and she can correct it by filling text in.
        self.fail('write me!')
