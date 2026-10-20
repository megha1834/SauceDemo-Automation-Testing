
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_backpack(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        ).click()

    def add_bike_light(self):
        self.page.locator(
            "[data-test='add-to-cart-sauce-labs-bike-light']"
        ).click()

    def remove_backpack(self):
        self.page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        ).click()

    def cart_badge(self):
        return self.page.locator(
            "[data-test='shopping-cart-badge']"
        )

    def open_cart(self):
        self.page.locator(
            "[data-test='shopping-cart-link']"
        ).click()
