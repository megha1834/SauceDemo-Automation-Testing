
import pytest
from playwright.sync_api import expect


def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_password",
         "Username and password do not match"),

        ("", "secret_sauce",
         "Username is required"),

        ("standard_user", "",
         "Password is required"),

        ("", "",
         "Username is required"),

        ("unknown_user", "secret_sauce",
         "Username and password do not match"),
    ]
)
def test_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)

    assert login_page.is_error_visible()
    assert expected_error in login_page.get_error_message()

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
