
from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def start_checkout(self):
        self.page.locator(
            "[data-test='checkout']"
        ).click()

    def fill_information(self, first_name, last_name, postal_code):
        self.page.locator(
            "[data-test='firstName']"
        ).fill(first_name)

        self.page.locator(
            "[data-test='lastName']"
        ).fill(last_name)

        self.page.locator(
            "[data-test='postalCode']"
        ).fill(postal_code)

    def continue_checkout(self):
        self.page.locator(
            "[data-test='continue']"
        ).click()

    def finish_checkout(self):
        self.page.locator(
            "[data-test='finish']"
        ).click()

    def confirmation_message(self):
        return self.page.locator(
            "[data-test='complete-header']"
        )

    def error_message(self):
        return self.page.locator(
            "[data-test='error']"
        )
